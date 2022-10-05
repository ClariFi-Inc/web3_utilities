# -*- coding: utf-8 -*-
"""Check and auto-feed Chikn.farm Roostr.

This script will:
    - Check if the given wallet has any roosted Roostr on Chikn.farm
    - Check if the user is the owner of the Wallet and Roostr's
    - Check if the Roostr is able to be fed or is still 'digesting'
    - Check if there is enough $EGG to feed the current Roostr

You can run this script using the project's root directory Makefile task: avax_gas_fee_watcher
    $ make autofeed_roostr


"""
import requests
from decouple import config
from rich import print  # noqa
from rich.pretty import pprint
from web3 import Web3


def is_digesting(roostr_id):
    """Check if roostr is digesting or if it can be fed

    :param roostr_id:
    :return:
    """


def list_roostr(address):
    list_roostr_url = f"https://api.chikn.farm/api/wallet/{address}/roostr"
    response = requests.get(list_roostr_url)
    if response.status_code == 200:
        response_json = response.json()
        pprint(response_json)

        if "data" in response_json and response_json["data"] is not None:
            for roostr in response_json["data"]:
                print(
                    f"Roostr #{roostr['token']}\n"
                    f"\t{'Rarity':<10} {roostr['rarity']}\n"
                    f"\t{'Roosted':<10} {roostr['isRoosted']}\n"
                    f"\t{'Weight':<10} {roostr['kg']} KG\n"
                    f"\t{'Fert/Day':<10} {roostr['fertPerDay']}\n"
                )


if __name__ == "__main__":
    # get a list of the wallet's Roostr
    w3 = Web3(Web3.HTTPProvider(config("AVAX_HTTPS_PROVIDER_URL")))
    w3.eth.account.enable_unaudited_hdwallet_features()

    list_roostr(config("AVAX_WALLET_ADDRESS"))
