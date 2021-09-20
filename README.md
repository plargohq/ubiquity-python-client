# ubiquity-python-client
A Python client to the Ubiquity service of blockdaemon.com.

# Requirements
Python 3.7.2 or newer.

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
$ make test
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

## Working with transactions

### Transaction creation and signing
Transactions can be created and signed directly from the SDK.
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

signed_tx = tx.create_and_sign(from_, to, key, { "network": network, "platform": platform })
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

# Note: Ethereum transactions don't contain an input address
from_ = [{
    "index: 3" # nonce
}]
to = [{
    "address": "<destination address>",
    "amount": 10 ** 18 # 1 ETH in smallest possible units (wei)
}]
fee = 21000

api_client = ApiClient(ubiquity.Configuration(
    host="<url>",
    access_token="<token>"
))

# An ApiClient object has to be passed to create_and_sign
#   for Ethereum because the gas price needs to be
#   fetched from the ethereum network
signed_tx = tx.create_and_sign(from_, to, key, {
    "api_client": api_client,
    "platform" platform,
    "network": network,
    "fee": fee
})

api_client.close()
print('signed: ', signed_tx)
```
For Ethereum only transactions with a single output are currently supported.

#### Broadcasting signed transactions
After a transaction is created and signed, it can be broadcasted through Ubiquity's `/tx/send` endpoint, that is interfaced through the `tx_send` method:

```python
conf = ubiquity.Configuration(
    host="url",
    access_token="token"
)

with ubiquity.ApiClient(conf) as api_client:
    api_instance = ubiquity.api.transactions_api.TransactionsApi(api_client)
    try:
        # Submit a signed transaction
        print("Sending signed transaction...")
        api_response = api_instance.tx_send(platform, network, signed_tx)
        print(api_response)
        print("Transaction sent successfully with id:", api_response.id)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->tx_send: %s\n" % e)

```

#### Estimating fees
Ubiquity's `/tx/estimate_fee` endpoint returns an estimation of the fee value required for transactions to be pushed to the network.
It can be used through the `TransactionsApi.estimate_fee` method:

```python
with ubiquity.ApiClient(config) as api_client:
    api_instance = ubiquity.api.transactions_api.TransactionsApi(api_client)
    try:
        # For bitcoin, the 'confirmed_within_blocks' parameter (defaults to 10) specifies
        #   the number of blocks the transaction would be processed within, which
        #   reflects in different fee values
        api_response = api_instance.estimate_fee("bitcoin", "testnet", confirmed_within_blocks=15)
        print("Fee value:", api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->estimate_fee: %s\n" % e)
```

## Websockets support

Ubiquity also supports websockets connections (see [docs](https://app.blockdaemon.com/docs/ubiquity#ubiquity-web-sockets-api)).
A client can communicate with this service to get notifications about new data from the network.

See the following example to subscribe to events for new blocks added to the network:

```python
import asyncio

from ubiquity import websockets as ws
from ubiquity import Configuration

async def run_client():
    conf = Configuration(
        host="<ws_url>",
        access_token="<token>"
    )

    # The class BlocksWebsocketConnection has the 'subscribe_blocks' method
    #   to interface the connection to the "ubiquity.blocks" channel:
    blocks_ws_connection = ws.BlocksWebsocketConnection()
    conn = blocks_ws_connection.connect(conf)

    # The function passed as callback is called when a new event is sent by the server
    #   in this example this function just prints the new block's id and height
    await blocks_ws_connection.subscribe_blocks(
        conn,
        1,
        lambda blk: print(blk['content']['id'], blk['content']['number'])
    )


asyncio.get_event_loop().run_until_complete(run_client())
```

The following table lists the classes and methods used to handle each websocket channel exposed by Ubiquity:

| Channel                     | Class                      | Method               |
| --------------------------- | -------------------------- | -------------------- |
| `ubiquity.blocks`            | BlocksWebsocketConnection   | `subscribe_blocks`    |
| `ubiquity.block_identifiers` | BlockIdsWebsocketConnection | `subscribe_block_ids` |
| `ubiquity.txs`               | TxsWebsocketConnection      | `subscribe_txs`       |

## Docs
Additional documentation and examples can be found in the `docs` directory.
