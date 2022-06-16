# -*- coding: utf-8 -*-
"""Get latest Avalanche block transaction data.

This script shows an example of how to call the Avalanche HTTPS RPC node to retrieve the network's
current block and transaction information

You can run this script using the project's root directory Makefile task: avax_gas_fee_watcher
    $ make avax_get_current_block

The script will output the latest avalanche network's block data

"""
from decouple import config
from hexbytes import HexBytes
from rich import print
from rich.pretty import pprint
from web3 import Web3
from web3.middleware import geth_poa_middleware

if __name__ == "__main__":
    w3 = Web3(Web3.HTTPProvider(config("AVAX_HTTPS_PROVIDER_URL")))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # get the latest transaction block from the avalanche rpc endpoint
    # Setting full_transactions=True
    # results in the return of the block's detailed transaction data.
    block = w3.eth.get_block("latest", full_transactions=True)

    # use rich.pprint to output the full data
    pprint(dict(block))

    """
    loop through each transaction, outputting
        - the transaction hash
        - the 'from' address
        - the 'to' address
    """
    for transaction in block["transactions"]:
        # the hash will be in HexBytes format, we
        # convert it using HexBytes.hex so it will display nicely
        tx_hash = HexBytes.hex(transaction["hash"])

        # output the information
        print(f"{tx_hash} sent From: {transaction['from']} To: {transaction['to']}")
