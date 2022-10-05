# -*- coding: utf-8 -*-
"""Check Chikn.farm Farmland Resources.

You can run this script using the project's root directory Makefile task: avax_gas_fee_watcher
    $ make farmland_resource_info


"""
import csv
import json

import constants
import requests
from rich import print  # noqa
from rich.pretty import pprint  # noqa

if __name__ == "__main__":

    CSV_HEADER_ROW = [
        "ID",
        "Name",
        "Rarity",
        "Rarest Tile",
        "For Sale",
        "Sale Price",
        "Last Price",
        "Bigness",
        "Size",
        "Fertility",
        "Multiplier",
        "Score",
        "Avg/Tile",
        "Dark Matter",
        "Avaxium",
        "Gold",
        "Mana",
        "Tungsten",
        "Mech",
        "Liquidium",
        "Veg",
        "Lumber",
        "Stone",
        "pyramid_Annuit",
        "pyramid_Avax",
        "BoneDaddy",
        "Goldmine",
        "ChiknMountain",
        "Excalibur",
        "Meteor",
        "Tungsten",
        "Ruin",
        "Red_Windmill",
        "Golf",
        "Graveyard",
        "HelicopterPad",
        "Mountain_Crystal",
        "BigHole",
        "Old_Windmill",
        "Water",
        "SmallFarm_Wheat_Fence",
        "Mountain",
        "Pond_Circle",
        "Pond_Corner",
        "Corn",
        "SmallFarm_Corn",
        "SmallFarm_Corn_Fence",
        "SmallFarm_Cabbage",
        "SmallFarm_Cabbage_Fence",
        "SmallFarm_Empty",
        "Grass_Mushrooms",
        "SmallFarm_Wheat",
        "Wheat",
        "Woods",
        "Roqs",
        "CoqRoqs",
        "Tasty Feed",
        "Orchard",
        "Hills",
        "Meadow",
        "Grass_Trees",
        "Grass_Full",
        "Grass_Thin",
    ]

    first_farmland_id = 1
    farmland_list = []

    with open(
        "farmland_data.csv",
        "r",
    ) as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            first_farmland_id = row[0]
            farmland_list.append(row)

        # add an additional for zero based arraw
        first_farmland_id += 1

    try:
        for farmland_id in range(first_farmland_id, 5001):
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
            for tile in farmland_json["tiles"]:
                # increase the count of this tile type for the farmland
                temp_list[CSV_HEADER_ROW.index(tile["tile"])] += 1

                # set the rarity of the farmland based on most rare tile
                if constants.CHIKN_RARITY_LIST.index(tile["rarity"]) < constants.CHIKN_RARITY_LIST.index(highest_rarity):
                    highest_rarity = tile["rarity"]
                temp_list[CSV_HEADER_ROW.index("Rarest Tile")] = highest_rarity

                # set the resource count for this tile type
                for resource in constants.FARMLAND_TILE_DICT[tile["tile"]]["resources"]:
                    temp_list[CSV_HEADER_ROW.index(resource["name"])] += 1

            farmland_list.append(temp_list)

    except Exception as ex:
        print(ex)

    finally:
        with open("farmland_data.json", "w") as f:
            json.dump(farmland_list, f)

        with open(
            "farmland_data.csv",
            "w",
        ) as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(CSV_HEADER_ROW)
            for farmland_row in farmland_list:
                csv_writer.writerow(farmland_row)

    # now write the date to a csv file
    # for farmland in farmland_list:
