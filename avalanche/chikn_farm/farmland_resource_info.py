# -*- coding: utf-8 -*-
"""Check Chikn.farm Farmland Resources.

You can run this script using the project's root directory Makefile task: avax_gas_fee_watcher
    $ make farmland_resource_info


"""
import sys

import requests
from constants import FARMLAND_TILE_DICT
from decouple import config
from rich import print  # noqa


def get_farmland_data(farmland_id):
    api_url = f"https://api.chikn.farm/api/farmland/details/{farmland_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        farmland_json = response.json()
        resource_dict = {}
        no_resource_dict = {}
        print(
            f"\n\nFarmland #{farmland_json['token']}\n"
            f"\t{'Bigness':<10} {farmland_json['bigness']}\n"
            f"\t{'Size':<10} {farmland_json['size']}\n"
            f"\t{'Fertility':<10} {farmland_json['fertility']}\n"
            f"\t{'Multiplier':<10} {farmland_json['multiplier']}"
        )
        print("\n\tTILES")
        print("\t============================================")
        for tile in farmland_json["tiles"]:
            print(f"\t{tile['tile']} - {tile['rarity']} | " f"({tile['score']} / {tile['percentile']}%)")

            if tile["tile"] in FARMLAND_TILE_DICT:
                if len(FARMLAND_TILE_DICT[tile["tile"]]["resources"]) == 0:
                    if tile["tile"] not in no_resource_dict:
                        no_resource_dict[tile["tile"]] = {"count": 0}
                    no_resource_dict[tile["tile"]]["count"] += 1
                for resource in FARMLAND_TILE_DICT[tile["tile"]]["resources"]:
                    if resource["name"] not in resource_dict:
                        resource_dict[resource["name"]] = {
                            "count": 0,
                            "tiles": {},
                        }
                    resource_dict[resource["name"]]["count"] += 1
                    if tile["tile"] not in resource_dict[resource["name"]]["tiles"]:
                        resource_dict[resource["name"]]["tiles"][tile["tile"]] = {"count": 0}
                    resource_dict[resource["name"]]["tiles"][tile["tile"]]["count"] += 1

            else:
                sys.exit(f"{tile['tile']} not found in tiles dict.")

        print("\n\tFarmland Tile Resources")
        print("\t============================================")
        for resource, data in resource_dict.items():
            print(f"\t{data['count']} {resource}")
            for tile, tile_data in data["tiles"].items():
                print(f"\t\t{tile_data['count']} {tile} Tiles")

        print("\n\tFarmland Tiles - No Resource Available")
        print("\t============================================")
        for tile, data in no_resource_dict.items():
            print(f"\t{data['count']} {tile}")


def list_farmlands(wallet_address):
    api_url = f"https://api.chikn.farm/api/wallet/{wallet_address}/farmland"
    response = requests.get(api_url)
    if response.status_code == 200:
        response_json = response.json()
        if "data" in response_json and response_json["data"] is not None:
            for farmland in response_json["data"]:
                token_id = farmland["token"]
                get_farmland_data(token_id)


if __name__ == "__main__":
    """By default, If no arguments are supplied, this script will use the avax wallet address to get detail on all of that wallets
    farmland.

    Optionally, sending in an integer on the command line will retrieve that specific farmland data.
    """
    args = sys.argv[1:]

    if len(args) > 0:
        # get the first argument and assume it's a farmland ID
        try:
            farmland_id = int(args[0])
            if farmland_id < 1 or farmland_id > 5000:
                sys.exit("Please supply a valid farmland ID")

            # ok, should be good, go get that farmland's data
            get_farmland_data(farmland_id)

        except Exception:
            sys.exit("Please supply a valid farmland ID")

    else:
        # no farmland id was supplied, get all the farmland for the wallet address, set in the .env file.
        list_farmlands(config("AVAX_WALLET_ADDRESS"))
