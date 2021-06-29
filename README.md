# ubiquity-python-client
A Python client to the Ubiquity service of blockdaemon.com.

# Requirements
Python 3.6 or newer.

# Installation

To install in your global Python installation with [pip](https://pip.pypa.io/en/stable/), run the following from the repository's root:

```bash
$ pip install -e .
```

To install using virtual environments:

```bash
$ python -m venv env
$ source testenv/bin/activate
$ pip install -e .
```

## Testing
To run the test suite first install the test dependencies with pip then run `pytest` at the repository's root:

```bash
$ pip install -r test-requirements.txt
$ make clean_generated
$ pytest
```

# Usage

## Basic

```python
import ubiquity
from ubiquity.api import blocks_api

conf = ubiquity.Configuration(
    access_token="<token>"
)

with ubiquity.ApiClient(conf) as client:
    blocks_api_instance = blocks_api.BlocksApi(client)
    platform = "ethereum"
    network = "mainnet"

    block = blocks_api_instance.get_block(platform, network, "current")
```

An API URL may also be specified if you have a personal ubiquity endpoint 

```python
import ubiquity
from ubiquity.api import blocks_api

conf = ubiquity.Configuration(
    host="<url>",
    access_token="<token>"
)

with ubiquity.ApiClient(conf) as client:
    blocks_api_instance = blocks_api.BlocksApi(client)
    platform = "ethereum"
    network = "mainnet"

    block = blocks_api_instance.get_block(platform, network, "current")
```


## Paginated API's

Certain resources contain more data than can practically returned in a single request. In these resources the data is split across multiple responses where each response returns a subset of the items requested and a continuation token. Requests for the first page of data should not contain a continuation token. To get the next batch of items the continuation token should be passed with the subsequent request. If no continuation token is returned all of the available data has been returned.

Initial request to paged API's should not include a continuation. If no limit is supplied the default of 25 will be applied.

```python
import ubiquity
from ubiquity.api import transactions_api

conf = ubiquity.Configuration(
    host="url",
    access_token="token"
)

with ubiquity.ApiClient(conf) as client:
    platform = "bitcoin"
    network = "mainnet"

    txs_api_instance = transactions_api.TransactionsApi(client)

    order = "desc"
    limit = 10

    txPage1 = txs_api_instance.get_txs(platform, network, order=order, limit=limit);
    continuation = txPage1['continuation']

    txPage2 = txs_api_instance.get_txs(platform, network, order=order, limit=limit, continuation=continuation);
```

To continue through the pages of transactions the continuation from the previous page must be supplied to the next request:

```python
with ubiquity.ApiClient(conf) as client:
    platform = "bitcoin"
    network = "mainnet"

    txs_api_instance = transactions_api.TransactionsApi(client)

    order = "desc"
    limit = 10

    txPage1 = txs_api_instance.get_txs(platform, network, order=order, limit=limit);
    continuation = txPage1['continuation']

    txPage2 = txs_api_instance.get_txs(platform, network, order=order, limit=limit, continuation=continuation);
```

## Transaction creation and signing
You can also create and sign transactions directly from the SDK.
Currently supported platforms are Bitcoin and Ethereum.

To create and sign a transaction that sends 0.0001 BTC (10000 satoshis) with a 0.00001 BTC (1000 satoshis) fee from an account to another:
```python
import ubiquity.transaction as tx

key = "<key>"

from_ = [{
    "address": "<input transaction>",
    "index": 0
}]
to = [
    {
        "address": "<destination address>",
        "amount": 10000
    }
]
fee = 1000

platform = "bitcoin"
network = "testnet" # can be "mainnet" or "testnet"

signed_tx = tx.create_and_sign(from_, to, fee, key, { "network": network, "platform": platform })
```

For Bitcoin an unsigned transaction can also be created with the function `ubiquity.transaction.create`.

To create and sign a transaction that sends 1 ETH and pays 21000 gas as fee from an account to another:
```python
import ubiquity
import ubiquity.transaction as tx
from ubiquity.api import ApiClient

platform = "ethereum"
network = "ropsten" # can be "mainnet" or "testnet"

key = "<key>"

from_ = [] # Ethereum transactions don't contain an input address
to = [{
    "address": "<destination address>",
    "amount": 10 ** 18 # 1 ETH in smallest possible units (wei)
}]
index = 3 # nonce
fee = 21000

api_client = ApiClient(ubiquity.Configuration(
    host="<url>",
    access_token="<token>"
))

# An ApiClient object has to be passed to create_and_sign
#   for Ethereum because the gas price needs to be
#   fetched from the ethereum network
signed_tx = tx.create_and_sign(from_, to, fee, key, {
    "api_client": api_client,
    "platform" platform,
    "network": network
})

api_client.close()
print('signed: ', signed_tx)
```
For Ethereum only transactions with a single output are currently supported.

## Docs
Additional documentation and examples can be found in the `docs` directory.
