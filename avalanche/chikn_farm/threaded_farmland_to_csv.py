# -*- coding: utf-8 -*-
"""Check Chikn.farm Farmland Resources.

You can run this script using the project's root directory Makefile task: avax_gas_fee_watcher
    $ make farmland_resource_info


"""
import csv
import sys
import time
from concurrent import futures
from os.path import exists

import constants
import requests
from rich import print  # noqa
from rich.pretty import pprint  # noqa

MAX_RETRIES = 5
COUNT_FARMLAND = 5000
MAX_WORKERS = 10
NUMBER_PER_THREAD = int(COUNT_FARMLAND / MAX_WORKERS)


def get_farmland_data(farmland_id, count_fail=None):
    if count_fail is None:
        count_fail = 0
        print(farmland_id)

    temp_list = []
    try:
        api_url = f"https://api.chikn.farm/api/farmland/details/{farmland_id}"

        # only wait max 5 seconds for a reply, we may get rate limited
        # and need to wait to call the API endpoint again.
        response = requests.get(api_url, timeout=5)
        if response.status_code != 200:
            # raise an exception so we retry this one.
            raise Exception(f"API returned {response.status_code}, retry this one!")
        else:
            farmland_json = response.json()

            name = farmland_json["name"] if farmland_json["name"] is not None else ""
            sale_price = 0
            last_price = 0
            rarity = ""

            if farmland_json["forSale"]:
                sale_price = farmland_json["salePrice"]
            if farmland_json["previousPrice"] is not None:
                last_price = farmland_json["previousPrice"]

            if farmland_json["rarity"] is not None:
                rarity = farmland_json["rarity"]

            temp_list = [
                farmland_id,
                name,
                rarity,
                "",
                farmland_json["forSale"],
                sale_price,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                last_price,
                farmland_json["bigness"],
                farmland_json["size"],
                farmland_json["fertility"],
                farmland_json["multiplier"],
                farmland_json["score"],
                farmland_json["averagePerTile"],
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ]

            highest_rarity = "Common"
            count_foragable_tiles = 0
            unique_tile_list = []
            unique_resource_list = []

            for tile in farmland_json["tiles"]:
                # increase the count of this tile type for the farmland
                temp_list[constants.FARMLAND_CSV_HEADER_ROW.index(tile["tile"])] += 1

                # add to unique tile list if needed
                if tile["tile"] not in unique_tile_list:
                    unique_tile_list.append(tile["tile"])

                # set the rarity of the farmland based on most rare tile
                if constants.CHIKN_RARITY_LIST.index(tile["rarity"]) < constants.CHIKN_RARITY_LIST.index(highest_rarity):
                    highest_rarity = tile["rarity"]

                # set the resource count for this tile type
                for resource in constants.FARMLAND_TILE_DICT[tile["tile"]]["resources"]:
                    temp_list[constants.FARMLAND_CSV_HEADER_ROW.index(resource["name"])] += 1

                    if resource["name"] not in unique_resource_list:
                        unique_resource_list.append(resource["name"])

                    count_foragable_tiles += 1

            temp_list[constants.FARMLAND_CSV_HEADER_ROW.index("Rarest Tile")] = highest_rarity
            temp_list[constants.FARMLAND_CSV_HEADER_ROW.index("# Resources")] = count_foragable_tiles
            temp_list[constants.FARMLAND_CSV_HEADER_ROW.index("# Unique Resources")] = len(unique_resource_list)
            temp_list[constants.FARMLAND_CSV_HEADER_ROW.index("# Unique Foragable Tiles")] = len(unique_tile_list)

    except Exception as get_ex:
        print(get_ex)
        count_fail += 1

        # retry MAX_RETRIES times
        if count_fail > MAX_RETRIES:
            # failed too many times, give up on this one.
            print(f"Failed to get farmland: {farmland_id}")

        else:
            if count_fail == 1:
                sleep_time = 10
            elif count_fail == 2:
                sleep_time = 15
            else:
                sleep_time = 20

            print(f"{farmland_id}: Retrying - #{count_fail} - sleeping {sleep_time} seconds")
            time.sleep(sleep_time)

            # retry getting this farmland
            temp_list = get_farmland_data(farmland_id, count_fail=count_fail)

    return temp_list


def fetch_farmland_by_range(farmland_range):
    farmland_list = []
    for farmland_id in range(farmland_range[0], farmland_range[1] + 1):
        if farmland_id > 5000:
            break

        temp_list = get_farmland_data(farmland_id)
        if len(temp_list) > 0:
            farmland_list.append(temp_list)

    return farmland_list


if __name__ == "__main__":
    FARMLAND_ID = None
    if len(sys.argv) > 1:
        try:
            FARMLAND_ID = int(sys.argv[1])
        except Exception:
            sys.exit(f"Invalid farmland id supplied.  Please supply an integer between 1 and {COUNT_FARMLAND}")

    # set the range based on a static number of records
    FARMLAND_RANGE_LIST = []

    previous_range_start = 1
    last_range_number = 5000 + NUMBER_PER_THREAD
    for i in range(100, last_range_number, NUMBER_PER_THREAD):
        FARMLAND_RANGE_LIST.append((previous_range_start, i))
        previous_range_start = i + 1

    if len(FARMLAND_RANGE_LIST) > MAX_WORKERS:
        MAX_WORKERS = len(FARMLAND_RANGE_LIST)

    farmland_list = []
    first_farmland_id = 1

    # if you want to run on just ONE farmland id, uncomment this and set the farmland Id you want
    if FARMLAND_ID is not None:
        FARMLAND_ID = 774
        MAX_WORKERS = 1
        FARMLAND_RANGE_LIST = [
            (FARMLAND_ID, FARMLAND_ID),
        ]

    if exists("farmland_data.csv"):
        with open(
            "farmland_data.csv",
            "r",
        ) as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                first_farmland_id = int(row[0])
                farmland_list.append(row)

    try:
        with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_farmland_range = dict((executor.submit(fetch_farmland_by_range, range), range) for range in FARMLAND_RANGE_LIST)

            for future in futures.as_completed(future_to_farmland_range):
                farmland_range = future_to_farmland_range[future]
                if future.exception() is not None:
                    print(f"Range: {farmland_range} generated an exception: {future.exception()}")
                else:
                    for result in future.result():
                        farmland_list.append(result)
    except Exception as ex:
        print(ex)

    finally:
        # sort farmland_list by farmland id
        sorted(farmland_list)

        # and save the data to the file.

        with open(
            "farmland_data.csv",
            "w",
        ) as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(constants.FARMLAND_CSV_HEADER_ROW)
            for farmland_row in farmland_list:
                csv_writer.writerow(farmland_row)
