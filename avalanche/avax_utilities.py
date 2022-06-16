import requests
from web3 import Web3


def get_max_fee_per_gas(provider_url: str, w3: Web3) -> int:
    """Determine the maxGasFee to use on a transaction based on current network state

    This method calls the eth_baseFee rpc call using python requests and returns the max gas fee

    :param :str provider_url: The network node endpoint to use
    :param :HTTPProvider provider: An optional HTTPProvider, will be utilized if sent in
    :return: int: the base gas fee
    """

    current_gas_fee = get_current_gas_fee(provider_url)

    # add 25 wei to the current gas fee to get the upper limit
    # Note: This is not the most efficient nor least expensive way to accomplish
    # this, however it works for most cases.  DYOR.
    current_gas_fee += w3.toWei(25, "gwei")
    return current_gas_fee


def get_current_gas_fee(provider_url: str) -> int:
    """Determine the maxGasFee to use on a transaction based on current network state

    This method calls the eth_baseFee rpc call using python requests and returns the max gas fee

    :param :str provider_url: The network node endpoint to use
    :param :HTTPProvider provider: An optional HTTPProvider, will be utilized if sent in
    :return: int: the base gas fee or None
    """

    # call the jsonprc endpoint using python requests
    # the eth_baseFee method does not exist on web3.py at this time.
    response = requests.post(
        provider_url,
        json={"jsonrpc": "2.0", "method": "eth_baseFee", "params": [], "id": 1},
    )

    response_json = response.json()

    if "result" not in response_json:
        raise Exception("Unable to retrieve eth_baseFee")
    else:
        # the received response will be in Hex, so
        # convert from hex to int, and return that value.
        return int(response.json()["result"], 16)
