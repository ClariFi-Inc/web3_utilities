# -*- coding: utf-8 -*-
"""Check Chikn.farm Chikn Traits.

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
COUNT_CHIKN = 10000
MAX_WORKERS = 10
NUMBER_PER_THREAD = int(COUNT_CHIKN / MAX_WORKERS)


def get_chikn_data(chikn_id, count_fail=None):
    if count_fail is None:
        count_fail = 0
        print(chikn_id)

    temp_list = []

    if chikn_id > COUNT_CHIKN:
        return temp_list

    try:
        api_url = f"https://api.chikn.farm/api/chikn/details/{chikn_id}"

        # only wait max 5 seconds for a reply, we may get rate limited
        # and need to wait to call the API endpoint again.
        response = requests.get(api_url, timeout=5)
        if response.status_code != 200:
            # raise an exception so we retry this one.
            if response.status_code == 400:
                # this chikn doesn't exist!
                print(f"NO chikn:   chikn {chikn_id} - skipping")
                return temp_list

            raise Exception(f"API returned {response.status_code}, retry this one!")
        else:
            chikn_json = response.json()
            name = chikn_json["name"] if chikn_json["name"] is not None else ""
            sale_price = 0
            last_price = 0
            rarity = ""
            egg_per_day = 0

            if chikn_json["forSale"]:
                sale_price = chikn_json["salePrice"]
            if chikn_json["previousPrice"] is not None:
                last_price = chikn_json["previousPrice"]

            if chikn_json["eggPerDay"] is not None:
                egg_per_day = chikn_json["eggPerDay"]

            flavour = chikn_json["flavour"] if chikn_json["flavour"] is not None else ""
            lore = chikn_json["lore"] if chikn_json["lore"] is not None else ""

            if chikn_json["rarity"] is not None:
                rarity = chikn_json["rarity"]

            head = chikn_json["head"]
            neck = chikn_json["neck"]
            torso = chikn_json["torso"]
            feet = chikn_json["feet"]
            tail = chikn_json["tail"]
            body = chikn_json["body"]
            trim = chikn_json["trim"]
            background = chikn_json["background"]

            highest_rarity = "Common"
            if head != "":
                head_rarity = constants.CHIKN_TRAIT_DICT["HEAD"][head]["rarity"]

                if constants.CHIKN_RARITY_LIST.index(head_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = head_rarity
            if neck != "":
                neck_rarity = constants.CHIKN_TRAIT_DICT["NECK"][neck]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(neck_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = neck_rarity
            if torso != "":
                torso_rarity = constants.CHIKN_TRAIT_DICT["TORSO"][torso]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(torso_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = torso_rarity
            if feet != "":
                feet_rarity = constants.CHIKN_TRAIT_DICT["FEET"][feet]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(feet_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = feet_rarity
            if tail != "":
                tail_rarity = constants.CHIKN_TRAIT_DICT["TAIL"][tail]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(tail_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = tail_rarity
            if body != "":
                body_rarity = constants.CHIKN_TRAIT_DICT["BODY"][body]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(body_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = body_rarity
            if trim != "":
                trim_rarity = constants.CHIKN_TRAIT_DICT["TRIM"][trim]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(trim_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = trim_rarity
            if background != "":
                background_rarity = constants.CHIKN_TRAIT_DICT["BACKGROUND"][background]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(background_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = background_rarity

            temp_list = [
                chikn_id,
                name,
                chikn_json["kg"],
                chikn_json["forSale"],
                sale_price,
                egg_per_day,
                rarity,
                chikn_json["_numOfTraits"],
                highest_rarity,
                head,
                neck,
                torso,
                feet,
                tail,
                body,
                trim,
                background,
                lore,
                flavour,
                chikn_json["rank"],
                chikn_json["score"],
                chikn_json["floorPrice"],
                last_price,
                chikn_json["isRoosted"],
            ]

    except Exception as get_ex:
        print(get_ex)
        count_fail += 1

        # retry MAX_RETRIES times
        if count_fail > MAX_RETRIES:
            # failed too many times, give up on this one.
            print(f"Failed to get chikn: {chikn_id}")

        else:
            if count_fail == 1:
                sleep_time = 10
            elif count_fail == 2:
                sleep_time = 15
            else:
                sleep_time = 20

            print(f"{chikn_id}: Retrying - #{count_fail} - sleeping {sleep_time} seconds")
            time.sleep(sleep_time)

            # retry getting this chikn
            temp_list = get_chikn_data(chikn_id, count_fail=count_fail)

    return temp_list


def fetch_chikn_by_range(chikn_range):
    chikn_list = []
    for chikn_id in range(chikn_range[0], chikn_range[1] + 1):
        if chikn_id > 12000:
            break

        temp_list = get_chikn_data(chikn_id)
        if len(temp_list) > 0:
            chikn_list.append(temp_list)

    return chikn_list


if __name__ == "__main__":
    chikn_ID = None
    if len(sys.argv) > 1:
        try:
            chikn_ID = int(sys.argv[1])
            if chikn_ID < 1 or chikn_ID > COUNT_CHIKN:
                sys.exit(f"Invalid chikn id supplied.  Please supply an integer between 1 and {COUNT_CHIKN}")
        except Exception:
            sys.exit(f"Invalid chikn id supplied.  Please supply an integer between 1 and {COUNT_CHIKN}")

    # set the range based on a static number of records
    chikn_RANGE_LIST = []

    previous_range_start = 1
    last_range_number = COUNT_CHIKN + NUMBER_PER_THREAD
    for i in range(100, last_range_number, NUMBER_PER_THREAD):
        chikn_RANGE_LIST.append((previous_range_start, i))
        previous_range_start = i + 1

    if len(chikn_RANGE_LIST) > MAX_WORKERS:
        MAX_WORKERS = len(chikn_RANGE_LIST)

    chikn_list = []
    first_chikn_id = 1

    # if you want to run on just ONE chikn id, uncomment this and set the chikn id you want
    if chikn_ID is not None:
        MAX_WORKERS = 1
        chikn_RANGE_LIST = [
            (chikn_ID, chikn_ID),
        ]

    if exists("chikn_data.csv"):
        with open(
            "chikn_data.csv",
            "r",
        ) as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                first_chikn_id = int(row[0])
                chikn_list.append(row)

    try:
        with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_chikn_range = dict((executor.submit(fetch_chikn_by_range, range), range) for range in chikn_RANGE_LIST)

            for future in futures.as_completed(future_to_chikn_range):
                chikn_range = future_to_chikn_range[future]
                if future.exception() is not None:
                    print(f"Range: {chikn_range} generated an exception: {future.exception()}")
                else:
                    for result in future.result():
                        chikn_list.append(result)
    except Exception as ex:
        print(ex)

    finally:
        # sort chikn_list by chikn id
        sorted(chikn_list)
        # and save the data to the file.

        with open(
            "chikn_data.csv",
            "w",
        ) as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(constants.CHIKN_CSV_HEADER_ROW)
            for chikn_row in chikn_list:
                csv_writer.writerow(chikn_row)
