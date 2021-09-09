from dataclasses import dataclass

import bitcoinlib.transactions as txs
import web3

from ubiquity.ubiquity_openapi_client.model.signed_tx import SignedTx
from ubiquity.api import (
    transactions_api,
    ApiClient,
)


# Custom exceptions
# ================================================
class TxVerificationError(Exception):
    pass


class TxCreationError(Exception):
    pass


class RequiredOptionError(Exception):
    def __init__(self, attr, options_dict):
        super().__init__(
            f"\"{attr}\" key not found in dictionary \"{options_dict}\"")


# ================================================


@dataclass
class UnsignedTx():
    id: str
    unsigned_tx: str

    def __post_init__(self):
        if type(self.id) != str:
            raise ValueError("'id' property should have type 'str'")
        if type(self.unsigned_tx) != str:
            raise ValueError("'unsigned_tx' property should have type 'str'")


def get_attr_from_opts(attr, options, default_val=None):
    if attr not in options:
        if default_val != None:
            return default_val
        raise RequiredOptionError(attr, options)

    return options[attr]


chain_ids = {"mainnet": 1, "ropsten": 3}


def create_and_sign_ethereum(from_, to, key, options):
    """
    Creates raw Bitcoin transaction and sign it with provided key.

    Parameters
    ----------
    from_ (list): List of dicts describing input transactions/addresses.
        - Each element is a dict with the following keys:
            - index (number): transaction nonce.
    to (list): List of dicts describing the transaction destination.
        - Each element is a dict with the following keys:
            - address (string): destination address.
            - amount (number): value to be transferred, in satoshis.
    key (string): private key used to sign the transaction.
    options (dict): options dictionary with the following keys:
        - network (string)
        - api_client (ubiquity.api.ApiClient): ApiClient instance used to fetch current gas price.
        - fee (number): fee to be paid for transaction in wei.
        - data (bytes): additional transaction data.
    ----------

    Returns:
    ----------
        signed_tx_str (string): the raw signed transaction string.
    ----------
    """
    api_client = get_attr_from_opts("api_client", options)
    network = get_attr_from_opts("network", options, "ropsten")
    fee = get_attr_from_opts("fee", options)
    data = get_attr_from_opts("data", options, b"")

    if len(to) > 1:
        raise TxCreationError(
            "Transactions with multiple outputs are currently not supported")

    from_obj = from_[0]
    to_obj = to[0]

    # Create api_instance to make call for getting gas_price
    api_instance = transactions_api.TransactionsApi(api_client)
    gas_price = int(api_instance.estimate_fee("ethereum", network))

    ETH_DECIMALS = 18
    amount = to_obj['amount'] // (10**ETH_DECIMALS)

    tx_dict = {
        "chainId": chain_ids[network],
        "nonce": from_obj['index'],
        "gasPrice": gas_price,
        "gas": fee,
        "to": to_obj['address'],
        "value": amount,
        "data": data
    }

    w3 = web3.Web3()
    signed_tx = w3.eth.account.sign_transaction(tx_dict, key)

    return signed_tx.rawTransaction.hex()


def create_bitcoin(from_, to, options):
    """
    Creates and returns a raw unsigned Bitcoin transaction

    Parameters
    ----------
    from_ (list): List of dicts describing input transactions/addresses.
        - Each element is a dict with the following keys:
            - address (string): input transaction.
            - index (number): input transaction index.
    to (list): List of dicts describing the transaction destination.
        - Each element is a dict with the following keys:
            - address (string): destination address.
            - amount (number): value to be transferred, in satoshis.
    options (dict): options dictionary with the following keys:
        - network (string)
    ----------

    Returns:
    ----------
        unsigned_tx_str (string): the raw unsigned transaction string.
    ----------
    """
    network = get_attr_from_opts('network', options)

    tx = txs.Transaction(network=network)

    for from_obj in from_:
        tx.add_input(prev_txid=from_obj['address'],
                     output_n=from_obj['index'],
                     compressed=False)

    for to_obj in to:
        tx.add_output(to_obj['amount'], to_obj['address'])

    return tx.raw_hex()


def create_and_sign_bitcoin(from_, to, key, options):
    """
    Creates raw Bitcoin transaction and sign it with provided key.

    Parameters
    ----------
    from_ (list): List of dicts describing input transactions/addresses.
        - Each element is a dict with the following keys:
            - address (string): input address.
            - index (number): transaction index for BTC or nonce for Ethereum.
    to (list): List of dicts describing the transaction destination.
        - Each element is a dict with the following keys:
            - address (string): destination address.
            - amount (number): value to be transferred, in satoshis.
    key (string): private key used to sign the transaction.
    options (dict): options dictionary with the following keys:
        - network (string)
    ----------

    Returns:
    ----------
        signed_tx_str (string): the raw signed transaction string.
    ----------
    """
    raw_tx = create_bitcoin(from_, to, options)

    network = get_attr_from_opts('network', options)

    tx = txs.transaction_deserialize(raw_tx, network=network)
    tx.sign(key)
    if not tx.verify():
        raise TxVerificationError(tx)
    return tx.raw_hex()


create_fns = {
    "bitcoin": create_bitcoin,
}

create_and_sign_fns = {
    "bitcoin": create_and_sign_bitcoin,
    "ethereum": create_and_sign_ethereum
}


def create(from_, to, options):
    """
    Creates and returns a raw unsigned transaction

    Parameters
    ----------
    from_ (list): List of dicts describing input transactions/addresses.
        - Each element is a dict with the following keys:
            - address (string): input address.
            - index (number): transaction index for BTC or nonce for Ethereum.
    to (list): List of dicts describing the transaction destination.
        - Each element is a dict with the following keys:
            - address (string): destination address.
            - amount (number): value to be transferred, in decimals (smallest possible unit for currency).
    options (dict): options dictionary with the following keys:
        - platform (string)
        - network (string)
        - api_client (ubiquity.api.ApiClient): ApiClient instance in case the there's some information that need to be fetched from the network.
        - fee (number): fee to be paid for transaction, in the smallest possible unit.
        - data (bytes): additional data the specific platform might use.
    ----------

    Returns:
    ----------
        unsigned_tx (UnignedTx): the unsigned transaction object.
    ----------
    """

    platform = get_attr_from_opts('platform', options)
    create_fn = create_fns[platform]

    raw_unsigned_tx = create_fn(from_, to, options)
    unsigned_tx_obj = txs.transaction_deserialize(raw_unsigned_tx)

    return UnsignedTx(id=unsigned_tx_obj.txid, unsigned_tx=raw_unsigned_tx)


def create_and_sign(from_, to, key, options):
    """
    Creates raw transaction and sign it with provided key.

    Parameters
    ----------
    from_ (list): List of dicts describing input transactions/addresses.
        - Each element is a dict with the following keys:
            - address (string): input address.
            - index (number): transaction index for BTC or nonce for Ethereum.
    to (list): List of dicts describing the transaction destination.
        - Each element is a dict with the following keys:
            - address (string): destination address.
            - amount (number): value to be transferred, in decimals (smallest possible unit for currency).
    key (string): private key used to sign the transaction.
    options (dict): options dictionary with the following keys:
        - platform (string)
        - network (string)
        - api_client (ApiClient): ApiClient instance in case the there's some information that need to be fetched from the network.
        - fee (number): fee to be paid for transaction, in the smallest possible unit.
        - data (bytes): additional data the specific platform might use.
    ----------

    Returns:
    ----------
        signed_tx (SignedTx): the signed transaction object.
    ----------
    """
    platform = get_attr_from_opts('platform', options)
    create_and_sign_fn = create_and_sign_fns[platform]
    raw_signed_tx = create_and_sign_fn(from_, to, key, options)

    return SignedTx(tx=raw_signed_tx)
