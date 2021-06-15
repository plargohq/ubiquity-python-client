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
    access_token="token"
)

with ubiquity.ApiClient(conf) as client:
    blocks_api_instance = blocks_api.BlocksApi(client)
    platform = "bitcoin"

    block = blocks_api_instance.get_block(platform, "current")
```

An API URL may also be specified if you have a personal ubiquity endpoint 

```python
import ubiquity
from ubiquity.api import blocks_api

conf = ubiquity.Configuration(
    host="url",
    access_token="token"
)

with ubiquity.ApiClient(conf) as client:
    blocks_api_instance = blocks_api.BlocksApi(client)
    platform = "bitcoin"

    block = blocks_api_instance.get_block(platform, "current")
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

    txs_api_instance = transactions_api.TransactionsApi(client)

    order = "desc"
    limit = 10

    txPage1 = txs_api_instance.get_txs(platform, order=order, limit=limit);
    continuation = txPage1['continuation']

    txPage2 = txs_api_instance.get_txs(platform, order=order, limit=limit, continuation=continuation);
```

To continue through the pages of transactions the continuation from the previous page must be supplied to the next request:

```python
with ubiquity.ApiClient(conf) as client:
    platform = "bitcoin"

    txs_api_instance = transactions_api.TransactionsApi(client)

    order = "desc"
    limit = 10

    txPage1 = txs_api_instance.get_txs(platform, order=order, limit=limit);
    continuation = txPage1['continuation']

    txPage2 = txs_api_instance.get_txs(platform, order=order, limit=limit, continuation=continuation);
```

## Docs
Additional documentation and examples can be found in the `docs` directory.
