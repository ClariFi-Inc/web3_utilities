# -*- coding: utf-8 -*-
"""Check Chikn.farm Farmland Resources.

You can run this script using the project's root directory Makefile task: avax_gas_fee_watcher
    $ make farmland_resource_info


"""
from decimal import Decimal

import requests
from constants import CHIKN_RARITY_LIST, FARMLAND_TILE_DICT
from rich import print  # noqa
from rich.pretty import pprint  # noqa

if __name__ == "__main__":

    """
    rarity_marketplace_dict = {}
    for rarity in CHIKN_RARITY_LIST:
        rarity_marketplace_dict[rarity] = {
            "sale_price": Decimal(9999999999),
            "farmland_id": 0,
        }
    """
    rarity_marketplace_dict = {
        "Unique": {"sale_price": Decimal("9999999999"), "farmland_id": 0},
        "Legendary": {"sale_price": 129, "farmland_id": 164},
        "Elite": {"sale_price": 49, "farmland_id": 650},
        "Rare": {"sale_price": 45, "farmland_id": 347},
        "Nice": {"sale_price": 29.5, "farmland_id": 434},
        "Common": {"sale_price": 24, "farmland_id": 209},
    }

    tile_marketplace_dict = {
        "pyramid_Annuit": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "pyramid_Avax": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "BoneDaddy": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Goldmine": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "ChiknMountain": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Excalibur": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Meteor": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Tungsten": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Ruin": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Red_Windmill": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Golf": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Graveyard": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "HelicopterPad": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Mountain_Crystal": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "BigHole": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Old_Windmill": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Water": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "SmallFarm_Wheat_Fence": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Mountain": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Pond_Circle": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Pond_Corner": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Corn": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "SmallFarm_Corn": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "SmallFarm_Corn_Fence": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "SmallFarm_Cabbage": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "SmallFarm_Cabbage_Fence": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "SmallFarm_Empty": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Grass_Mushrooms": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "SmallFarm_Wheat": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Wheat": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Woods": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Roqs": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "CoqRoqs": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Tasty Feed": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Orchard": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Hills": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Meadow": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Grass_Trees": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Grass_Full": {"sale_price": Decimal(999999999), "farmland_id": 0},
        "Grass_Thin": {"sale_price": Decimal(999999999), "farmland_id": 0},
    }

    """
    resource_marketplace_dict = {'Dark Matter': { 'sale_price': Decimal(999999999), 'farmland_id': 0},
     'Avaxium': {'sale_price': Decimal(9999999999), 'farmland_id': 0},
     'Gold': {'sale_price': Decimal(9999999999), 'farmland_id': 0},
     'Mana': { 'sale_price': Decimal(999999999), 'farmland_id': 0},
     'Tungsten': { 'sale_price': Decimal(999999999), 'farmland_id': 0},
     'Mech': { 'sale_price': Decimal(999999999), 'farmland_id': 0},
     'Liquidium': { 'sale_price': Decimal(999999999), 'farmland_id': 0},
     'Veg': { 'sale_price': Decimal(999999999), 'farmland_id': 0},
     'Lumber': { 'sale_price': Decimal(999999999), 'farmland_id': 0},
     'Stone': { 'sale_price': Decimal(999999999), 'farmland_id': 0}}
    """
    resource_marketplace_dict = {
        "Dark Matter": {"sale_price": 129, "farmland_id": 164},
        "Avaxium": {"sale_price": 100, "farmland_id": 965},
        "Gold": {"sale_price": 80, "farmland_id": 428},
        "Mana": {"sale_price": 38.42, "farmland_id": 800},
        "Tungsten": {"sale_price": 220, "farmland_id": 618},
        "Mech": {"sale_price": 29.5, "farmland_id": 434},
        "Liquidium": {"sale_price": 59, "farmland_id": 463},
        "Veg": {"sale_price": 26, "farmland_id": 179},
        "Lumber": {"sale_price": 24, "farmland_id": 209},
        "Stone": {"sale_price": 26, "farmland_id": 179},
    }

    for farmland_id in range(1170, 5001):
        print(farmland_id)
        api_url = f"https://api.chikn.farm/api/farmland/details/{farmland_id}"
        response = requests.get(api_url)

        if response.status_code == 200:
            farmland_json = response.json()
            # pprint(farmland_json)
            if farmland_json["forSale"]:
                highest_rarity = "Common"
                for tile in farmland_json["tiles"]:
                    if CHIKN_RARITY_LIST.index(tile["rarity"]) < CHIKN_RARITY_LIST.index(highest_rarity):
                        highest_rarity = tile["rarity"]

                    for resource in FARMLAND_TILE_DICT[tile["tile"]]["resources"]:
                        # print(resource)
                        # rint(resource_marketplace_dict[resource])
                        if resource_marketplace_dict[resource["name"]]["sale_price"] > farmland_json["salePrice"]:
                            resource_marketplace_dict[resource["name"]]["sale_price"] = farmland_json["salePrice"]
                            resource_marketplace_dict[resource["name"]]["farmland_id"] = farmland_id

                if rarity_marketplace_dict[highest_rarity]["sale_price"] > farmland_json["salePrice"]:
                    rarity_marketplace_dict[highest_rarity]["sale_price"] = farmland_json["salePrice"]
                    rarity_marketplace_dict[highest_rarity]["farmland_id"] = farmland_id

        if farmland_id % 10 == 0:
            pprint(rarity_marketplace_dict)
            pprint(resource_marketplace_dict)

    pprint(rarity_marketplace_dict)
    pprint(resource_marketplace_dict)
