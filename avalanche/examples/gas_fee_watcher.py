# -*- coding: utf-8 -*-
"""Retrieve current avax gas fee, every 3 seconds.

This script shows an example of how to call the Avalanche HTTPS RPC node to retrieve the network's current
gas fee

You can run this script using the project's root directory Makefile task: avax_gas_fee_watcher
    $ make avax_gas_fee_watcher

The script will output the avalanche network's current gas fee every 3 seconds.  Output will be similar to the following:

    $ 25.0000    11:43:58 am Jun 16, 2022
    $ 25.0000    11:44:01 am Jun 16, 2022
    $ 25.0000    11:44:05 am Jun 16, 2022
    $ 25.0000    11:44:08 am Jun 16, 2022

To quit/cancel the script press ^c.

"""
import time

import arrow
from decouple import config
from rich import print

from ..avax_utilities import get_current_gas_fee

FREQUENCY_SECONDS = 3

if __name__ == "__main__":
    """
    Run gas fee getter process every FREQUENCY_SECONDS until the users force-quits (^c) the process.
    """
    while True:
        gas_fee = get_current_gas_fee(config("AVAX_HTTPS_PROVIDER_URL"))
        # the gas fee is returned in nAVAX, so let's make it look nicer
        # by converting it to a float and remove some decimals
        gas_fee = gas_fee / (10**9)
        gas_fee = f"{gas_fee:.4f}"

        print(f"{gas_fee:<10} {arrow.now().format('h:mm:ss a MMM D, YYYY')}")

        # sleep the number of seconds and repeat
        time.sleep(FREQUENCY_SECONDS)
