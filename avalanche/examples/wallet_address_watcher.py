# -*- coding: utf-8 -*-
"""Watch a wallet address for activity

This script shows an example of how to watch a specific wallet address for activity

You can run this script using the project's root directory Makefile task: avax_gas_fee_watcher
    $ make wallet_address_watcher

To quit/cancel the script press ^c.

"""
import asyncio

from decouple import config
from rich import print
from rich.pretty import pprint
from web3 import HTTPProvider, Web3


def handle_event(event, w3):
    """Handle the event
    This will take the event captured in the filter and print it out.  Note that when filtering
    on a wallet address the event you receive will be a transaction

    :param event:
    :return:
    """

    # the event is the block number, so we need to go out and
    # get the block as well as the transaction data, so we'll do that

    pprint(event)

    # block = w3.eth.get_block(event, full_transactions=True)
    # pprint(block)


async def log_loop(event_filter, poll_interval, w3):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event, w3)
        await asyncio.sleep(poll_interval)


def main(w3):
    # we need to filter on the latest blocks, and then look at the transaction data to see if any
    # action has happened on a specific address
    latest_filter = w3.eth.filter("latest")
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(latest_filter, 2, w3),
            )
        )
    finally:
        loop.close()


if __name__ == "__main__":
    try:
        provider = HTTPProvider(config("AVAX_HTTPS_PROVIDER_URL"))
        w3 = Web3(provider)

        # start the main async loop
        print(f"STARTING WALLET ADDRESS WATCH FOR: {config('AVAX_WALLET_ADDRESS')} on node: {config('AVAX_HTTPS_PROVIDER_URL')}")

        main(w3)

    except Exception as ex:
        print(ex)

    finally:
        print("EXITING")
