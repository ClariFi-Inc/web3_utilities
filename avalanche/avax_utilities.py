import requests
from decouple import config
from rich.pretty import pprint  # noqa
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


def get_covalent_page_transactions(wallet_address, page_number, page_size=None):
    """Get a page of covalent transactions for a given wallet

    :param wallet_address:
    :param page_number:
    :param page_size:
    :return:
    """
    if page_size is None:
        page_size = 30

    covalent_api_url = (
        f"https://api.covalenthq.com/v1/43114/address/{wallet_address}"
        f"/transactions_v2/?quote-currency=USD&format=JSON&no-logs=false"
        f"&block-signed-at-asc=false"
        f"&page-number={page_number}"
        f"&page-size={page_size}"
        f"&key={config('COVALENT_API_KEY')}"
    )

    response = requests.get(covalent_api_url)
    response_json = response.json()

    has_more = False
    if "data" not in response_json or response_json["error"]:
        print("[bold red]Error with Covalent[/]\n")
        if "error_message" in response_json:
            print(f"[bold red]Covalent error response: {response_json['error_message']}[/]")

    if "pagination" in response_json["data"]:
        if response_json["data"]["pagination"] is not None:
            has_more = response_json["data"]["pagination"]["has_more"]

    if response_json["data"] is None:
        if response_json["error_code"] == 507:
            # the backend queue is full so need to wait a bit to kick it through
            pass

    transaction_list = []
    # check to see if we have already loaded data for this wallet, if we have, only gather the
    # transactions up to the last loaded transaction
    count_loaded = 0
    transaction_list = response_json["data"]["items"]
    count_loaded += len(transaction_list)

    return {"has_more": has_more, "json_data": transaction_list, "count_loaded": count_loaded}


def get_wallet_covalent_transaction_list(wallet_address):
    # go out to covalent for the wallet and get the latest transactions
    current_page = 0
    has_more = True
    count_transactions = 0
    transaction_list = []
    while has_more:
        results = get_covalent_page_transactions(wallet_address, current_page)
        has_more = results["has_more"]
        page_transactions = results["json_data"]
        count_transactions += results["count_loaded"]
        transaction_list += page_transactions
        current_page += 1

    # check to see if the first transaction is newer than the last transaction, if it is
    # we want to reverse the list so that it will be in ascending numerical order
    # if len(transaction_list) >= 2:
    #    first_txn_signed_at = arrow.get(transaction_list[0]["block_signed_at"]).datetime
    #    last_txn__signed_at = arrow.get(transaction_list[-1]["block_signed_at"]).datetime

    #     if first_txn_signed_at > last_txn__signed_at:
    #         transaction_list.reverse()

    return transaction_list


def get_last_contract_transaction_for_wallet(wallet_address, contract_address):
    # go out to covalent for the wallet and get the latest transactions
    current_page = 0
    has_more = True
    last_contract_transaction = None

    while has_more:
        results = get_covalent_page_transactions(wallet_address, current_page)
        has_more = results["has_more"]
        page_transactions = results["json_data"]
        for transaction in page_transactions:
            if transaction["to_address"].lower() == contract_address.lower():
                return transaction

    return last_contract_transaction
