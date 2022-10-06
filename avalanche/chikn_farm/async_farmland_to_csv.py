# -*- coding: utf-8 -*-
"""Check Chikn.farm Farmland Resources.

You can run this script using the project's root directory Makefile task: avax_gas_fee_watcher
    $ make farmland_resource_info


"""

import asyncio
import csv
from os.path import exists

import constants
import requests
from rich import print  # noqa
from rich.pretty import pprint  # noqa


def read_csv_file():
    farmland_list = []
    first_farmland_id = 1

    if exists("farmland_data.csv"):
        with open("farmland_data.csv", "r") as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                first_farmland_id = int(row[0])
                farmland_list.append(row)

            # add one to account for zero based array
            first_farmland_id += 1

    return farmland_list, first_farmland_id


def write_csv_file(farmland_list):
    # with open("farmland_data.json", "w") as f:
    #    json.dump(farmland_list, f)
    # print("Writing!")
    # pprint(farmland_list)
    with open("farmland_data.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(constants.FARMLAND_CSV_HEADER_ROW)
        for farmland_row in farmland_list:
            csv_writer.writerow(farmland_row)


async def fetch_farmland_in_range(start_token_id, end_token_id):
    farmland_list = []
    for farmland_id in range(start_token_id, end_token_id + 1):
        print(farmland_id)
        api_url = f"https://api.chikn.farm/api/farmland/details/{farmland_id}"
        response = requests.get(api_url)

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
            last_price,
            0,
            0,
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
        for tile in farmland_json["tiles"]:
            # increase the count of this tile type for the farmland
            temp_list[constants.FARMLAND_CSV_HEADER_ROW.index(tile["tile"])] += 1

            # add to unique tile list if needed
            if tile["tile"] not in unique_tile_list:
                unique_tile_list.append(tile["tile"])

            # set the rarity of the farmland based on most rare tile
            if constants.CHIKN_RARITY_LIST.index(tile["rarity"]) < constants.CHIKN_RARITY_LIST.index(highest_rarity):
                highest_rarity = tile["rarity"]
            temp_list[constants.FARMLAND_CSV_HEADER_ROW.index("Rarest Tile")] = highest_rarity

            # set the resource count for this tile type
            for resource in constants.FARMLAND_TILE_DICT[tile["tile"]]["resources"]:
                temp_list[constants.FARMLAND_CSV_HEADER_ROW.index(resource["name"])] += 1

                count_foragable_tiles += 1

        temp_list[constants.FARMLAND_CSV_HEADER_ROW.index("# Foragable")] = count_foragable_tiles
        temp_list[constants.FARMLAND_CSV_HEADER_ROW.index("# Unique Foragable")] = len(unique_tile_list)

        farmland_list.append(temp_list)

    return farmland_list


async def main():
    # load the csv file syncronously
    loop = asyncio.get_running_loop()
    farmland_list, first_farmland_id = await loop.run_in_executor(None, read_csv_file)

    try:
        farmland_list_1 = (await fetch_farmland_in_range(1, 10),)
        await fetch_farmland_in_range(11, 20)

        print(farmland_list_1)

        # full_farmland_list = farmland_list_1 + farmland_list_2

        # print(len(full_farmland_list))

    except Exception as ex:
        print("EXCEPTION!!!!")
        print(ex)

    finally:
        # print(len(farmland_list_1))
        # print(len(farmland_list_2))
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, write_csv_file, farmland_list)

    # now write the date to a csv file
    # for farmland in farmland_list:


asyncio.run(main())
