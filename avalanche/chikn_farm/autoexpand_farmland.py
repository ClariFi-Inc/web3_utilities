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

from ..avax_utilities import get_last_contract_transaction_for_wallet

FARMLAND_CONTRACT_ADDRESS = "0x00f5D01D86008D14d04E29EFe88DffC75a9cAc47"


def list_farmland(address):
    api_url = f"https://api.chikn.farm/api/wallet/{address}/farmland"
    response = requests.get(api_url)
    if response.status_code == 200:
        response_json = response.json()
        pprint(response_json)

        if "data" in response_json and response_json["data"] is not None:
            for farmland in response_json["data"]:
                print(
                    f"Farmland #{farmland['token']}\n" f"\t{'Bigness':<10} {farmland['bigness']}\n" f"\t{'Size':<10} {farmland['size']}\n"
                )


if __name__ == "__main__":
    # get a list of the wallet's Roostr
    w3 = Web3(Web3.HTTPProvider(config("AVAX_HTTPS_PROVIDER_URL")))
    w3.eth.account.enable_unaudited_hdwallet_features()

    # list_farmland(config('AVAX_WALLET_ADDRESS'))

    last_contract_transaction = get_last_contract_transaction_for_wallet(
        Web3.toChecksumAddress(config("AVAX_WALLET_ADDRESS")), Web3.toChecksumAddress(FARMLAND_CONTRACT_ADDRESS)
    )

    if last_contract_transaction is None:
        print(f"No contract transaction matching the contract address: {FARMLAND_CONTRACT_ADDRESS}")
    else:
        pprint(last_contract_transaction)
