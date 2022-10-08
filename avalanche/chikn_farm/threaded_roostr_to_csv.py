# -*- coding: utf-8 -*-
"""Check Chikn.farm Roostr Resources.

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
COUNT_ROOSTR = 12000
MAX_WORKERS = 10
NUMBER_PER_THREAD = int(12000 / MAX_WORKERS)


def get_roostr_data(roostr_id, count_fail=None):
    if count_fail is None:
        count_fail = 0
        print(roostr_id)

    temp_list = []
    try:
        api_url = f"https://api.chikn.farm/api/roostr/details/{roostr_id}"

        # only wait max 5 seconds for a reply, we may get rate limited
        # and need to wait to call the API endpoint again.
        response = requests.get(api_url, timeout=5)
        if response.status_code != 200:
            # raise an exception so we retry this one.
            if response.status_code == 400:
                # this roostr doesn't exist!
                print(f"NO ROOSTR:   ROOSTR {roostr_id} - skipping")
                return temp_list

            raise Exception(f"API returned {response.status_code}, retry this one!")
        else:
            roostr_json = response.json()
            name = roostr_json["name"] if roostr_json["name"] is not None else ""
            sale_price = 0
            last_price = 0
            rarity = ""
            fert_per_day = 0

            if roostr_json["forSale"]:
                sale_price = roostr_json["salePrice"]
            if roostr_json["previousPrice"] is not None:
                last_price = roostr_json["previousPrice"]

            if roostr_json["fertPerDay"] is not None:
                fert_per_day = roostr_json["fertPerDay"]

            flavour = roostr_json["flavour"] if roostr_json["flavour"] is not None else ""
            lore = roostr_json["lore"] if roostr_json["lore"] is not None else ""

            if roostr_json["rarity"] is not None:
                rarity = roostr_json["rarity"]

            head = roostr_json["head"]
            neck = roostr_json["neck"]
            torso = roostr_json["torso"]
            feet = roostr_json["feet"]
            tail = roostr_json["tail"]
            body = roostr_json["body"]
            trim = roostr_json["trim"]
            background = roostr_json["background"]

            highest_rarity = "Common"
            if head != "":
                head_rarity = constants.ROOSTR_TRAIT_DICT["HEAD"][head]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(head_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = head_rarity
            if neck != "":
                neck_rarity = constants.ROOSTR_TRAIT_DICT["NECK"][neck]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(neck_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = neck_rarity
            if torso != "":
                torso_rarity = constants.ROOSTR_TRAIT_DICT["TORSO"][torso]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(torso_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = torso_rarity
            if feet != "":
                feet_rarity = constants.ROOSTR_TRAIT_DICT["FEET"][feet]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(feet_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = feet_rarity
            if tail != "":
                tail_rarity = constants.ROOSTR_TRAIT_DICT["TAIL"][tail]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(tail_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = tail_rarity
            if body != "":
                body_rarity = constants.ROOSTR_TRAIT_DICT["BODY"][body]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(body_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = body_rarity
            if trim != "":
                trim_rarity = constants.ROOSTR_TRAIT_DICT["TRIM"][trim]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(trim_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = trim_rarity
            if background != "":
                background_rarity = constants.ROOSTR_TRAIT_DICT["BACKGROUND"][background]["rarity"]
                if constants.CHIKN_RARITY_LIST.index(background_rarity.upper()) < constants.CHIKN_RARITY_LIST.index(highest_rarity.upper()):
                    highest_rarity = background_rarity

            temp_list = [
                roostr_id,
                name,
                roostr_json["kg"],
                roostr_json["forSale"],
                sale_price,
                fert_per_day,
                rarity,
                roostr_json["_numOfTraits"],
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
                roostr_json["rank"],
                roostr_json["score"],
                roostr_json["floorPrice"],
                last_price,
                roostr_json["isRoosted"],
            ]

    except Exception as get_ex:
        print(get_ex)
        count_fail += 1

        # retry MAX_RETRIES times
        if count_fail > MAX_RETRIES:
            # failed too many times, give up on this one.
            print(f"Failed to get roostr: {roostr_id}")

        else:
            if count_fail == 1:
                sleep_time = 10
            elif count_fail == 2:
                sleep_time = 15
            else:
                sleep_time = 20

            print(f"{roostr_id}: Retrying - #{count_fail} - sleeping {sleep_time} seconds")
            time.sleep(sleep_time)

            # retry getting this roostr
            temp_list = get_roostr_data(roostr_id, count_fail=count_fail)

    return temp_list


def fetch_roostr_by_range(roostr_range):
    roostr_list = []
    for roostr_id in range(roostr_range[0], roostr_range[1] + 1):
        if roostr_id > 12000:
            break

        temp_list = get_roostr_data(roostr_id)
        if len(temp_list) > 0:
            roostr_list.append(temp_list)

    return roostr_list


if __name__ == "__main__":
    ROOSTR_ID = None
    if len(sys.argv) > 1:
        try:
            ROOSTR_ID = int(sys.argv[1])
            if ROOSTR_ID < 1 or ROOSTR_ID > COUNT_ROOSTR:
                sys.exit(f"Invalid roostr id supplied.  Please supply an integer between 1 and {COUNT_ROOSTR}")
        except Exception:
            sys.exit(f"Invalid roostr id supplied.  Please supply an integer between 1 and {COUNT_ROOSTR}")

    # set the range based on a static number of records
    ROOSTR_RANGE_LIST = []

    previous_range_start = 1
    last_range_number = COUNT_ROOSTR + NUMBER_PER_THREAD
    for i in range(100, last_range_number, NUMBER_PER_THREAD):
        ROOSTR_RANGE_LIST.append((previous_range_start, i))
        previous_range_start = i + 1

    if len(ROOSTR_RANGE_LIST) > MAX_WORKERS:
        MAX_WORKERS = len(ROOSTR_RANGE_LIST)

    roostr_list = []
    first_roostr_id = 1

    # if you want to run on just ONE roostr id, uncomment this and set the roostr id you want
    if ROOSTR_ID is not None:
        MAX_WORKERS = 1
        ROOSTR_RANGE_LIST = [
            (ROOSTR_ID, ROOSTR_ID),
        ]

    if exists("roostr_data.csv"):
        with open(
            "roostr_data.csv",
            "r",
        ) as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                first_roostr_id = int(row[0])
                roostr_list.append(row)

    # try:
    with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_roostr_range = dict((executor.submit(fetch_roostr_by_range, range), range) for range in ROOSTR_RANGE_LIST)

        for future in futures.as_completed(future_to_roostr_range):
            roostr_range = future_to_roostr_range[future]
            if future.exception() is not None:
                print(f"Range: {roostr_range} generated an exception: {future.exception()}")
            else:
                for result in future.result():
                    roostr_list.append(result)

    """
    except Exception as ex:
        print(ex)

    finally:
    """
    # sort roostr_list by roostr id
    sorted(roostr_list)

    # and save the data to the file.

    with open(
        "roostr_data.csv",
        "w",
    ) as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(constants.ROOSTR_CSV_HEADER_ROW)
        for roostr_row in roostr_list:
            csv_writer.writerow(roostr_row)
