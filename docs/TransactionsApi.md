# ubiquity.ubiquity_openapi_client.TransactionsApi

All URIs are relative to *https://ubiquity.api.blockdaemon.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fee_estimate**](TransactionsApi.md#fee_estimate) | **GET** /{platform}/{network}/tx/estimate_fee | Get fee estimate
[**get_tx**](TransactionsApi.md#get_tx) | **GET** /{platform}/{network}/tx/{id} | Transaction By Hash
[**get_tx_by_hash_and_index**](TransactionsApi.md#get_tx_by_hash_and_index) | **GET** /{platform}/{network}/tx/{id}/{index} | Transaction output by hash and index
[**get_tx_confirmations**](TransactionsApi.md#get_tx_confirmations) | **GET** /{platform}/{network}/tx/{id}/confirmations | Transaction confirmations By Hash
[**get_txs**](TransactionsApi.md#get_txs) | **GET** /{platform}/{network}/txs | Latest transactions of a protocol
[**tx_send**](TransactionsApi.md#tx_send) | **POST** /{platform}/{network}/tx/send | Submit a signed transaction


# **fee_estimate**
> FeeEstimate fee_estimate(platform, network)

Get fee estimate

Get a fee estimation in decimals from the ubiquity fee estimation service. Currently supported for Bitcoin and Ethereum. Endpoint will return 3 fee estimations fast, medium and slow 

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import transactions_api
from ubiquity.ubiquity_openapi_client.model.fee_estimate import FeeEstimate
from ubiquity.ubiquity_openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://ubiquity.api.blockdaemon.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    host = "https://ubiquity.api.blockdaemon.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ubiquity.ubiquity_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    platform = "bitcoin" # str | Coin platform handle
    network = "mainnet" # str | Which network to target. Available networks can be found with /{platform}

    # example passing only required values which don't have defaults set
    try:
        # Get fee estimate
        api_response = api_instance.fee_estimate(platform, network)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->fee_estimate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} |

### Return type

[**FeeEstimate**](FeeEstimate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Platforms overview |  -  |
**401** | Invalid or expired token |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tx**
> Tx get_tx(platform, network, id)

Transaction By Hash

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import transactions_api
from ubiquity.ubiquity_openapi_client.model.tx import Tx
from ubiquity.ubiquity_openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://ubiquity.api.blockdaemon.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    host = "https://ubiquity.api.blockdaemon.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ubiquity.ubiquity_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    platform = "bitcoin" # str | Coin platform handle
    network = "mainnet" # str | Which network to target. Available networks can be found with /{platform}
    id = "0xF00Fa860473130C1df10707223E66Cb4B839B165" # str | Transaction ID/Hash

    # example passing only required values which don't have defaults set
    try:
        # Transaction By Hash
        api_response = api_instance.get_tx(platform, network, id)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_tx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} |
 **id** | **str**| Transaction ID/Hash |

### Return type

[**Tx**](Tx.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction |  -  |
**400** | Bad Request |  -  |
**401** | Invalid or expired token |  -  |
**404** | Not Found |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tx_by_hash_and_index**
> TxOutput get_tx_by_hash_and_index(platform, network, id, index)

Transaction output by hash and index

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import transactions_api
from ubiquity.ubiquity_openapi_client.model.tx_output import TxOutput
from ubiquity.ubiquity_openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://ubiquity.api.blockdaemon.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    host = "https://ubiquity.api.blockdaemon.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ubiquity.ubiquity_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    platform = "bitcoin" # str | Coin platform handle
    network = "mainnet" # str | Which network to target. Available networks can be found with /{platform}
    id = "0xF00Fa860473130C1df10707223E66Cb4B839B165" # str | Transaction ID/Hash
    index = 0 # int | Transaction output index

    # example passing only required values which don't have defaults set
    try:
        # Transaction output by hash and index
        api_response = api_instance.get_tx_by_hash_and_index(platform, network, id, index)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_tx_by_hash_and_index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} |
 **id** | **str**| Transaction ID/Hash |
 **index** | **int**| Transaction output index |

### Return type

[**TxOutput**](TxOutput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction output |  -  |
**400** | Bad Request |  -  |
**401** | Invalid or expired token |  -  |
**404** | Not Found |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tx_confirmations**
> TxConfirmation get_tx_confirmations(platform, network, id)

Transaction confirmations By Hash

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import transactions_api
from ubiquity.ubiquity_openapi_client.model.error import Error
from ubiquity.ubiquity_openapi_client.model.tx_confirmation import TxConfirmation
from pprint import pprint
# Defining the host is optional and defaults to https://ubiquity.api.blockdaemon.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    host = "https://ubiquity.api.blockdaemon.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ubiquity.ubiquity_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    platform = "bitcoin" # str | Coin platform handle
    network = "mainnet" # str | Which network to target. Available networks can be found with /{platform}
    id = "0xF00Fa860473130C1df10707223E66Cb4B839B165" # str | Transaction ID/Hash

    # example passing only required values which don't have defaults set
    try:
        # Transaction confirmations By Hash
        api_response = api_instance.get_tx_confirmations(platform, network, id)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_tx_confirmations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} |
 **id** | **str**| Transaction ID/Hash |

### Return type

[**TxConfirmation**](TxConfirmation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction confirmations |  -  |
**400** | Bad Request |  -  |
**401** | Invalid or expired token |  -  |
**404** | Not Found |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_txs**
> TxPage get_txs(platform, network)

Latest transactions of a protocol

Gets transactions from oldest to newest. This call uses pagination. 

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import transactions_api
from ubiquity.ubiquity_openapi_client.model.error import Error
from ubiquity.ubiquity_openapi_client.model.tx_page import TxPage
from pprint import pprint
# Defining the host is optional and defaults to https://ubiquity.api.blockdaemon.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    host = "https://ubiquity.api.blockdaemon.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ubiquity.ubiquity_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    platform = "bitcoin" # str | Coin platform handle
    network = "mainnet" # str | Which network to target. Available networks can be found with /{platform}
    order = "desc" # str | Pagination order (optional)
    continuation = "8185.123" # str | Continuation token from earlier response (optional)
    limit = 25 # int | Max number of items to return in a response. Defaults to 25 and is capped at 100.  (optional)
    assets = "ethereum/native/eth" # str | Comma-separated list of asset paths to filter. If the list is empty, or all elements are empty, this filter has no effect. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Latest transactions of a protocol
        api_response = api_instance.get_txs(platform, network)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_txs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Latest transactions of a protocol
        api_response = api_instance.get_txs(platform, network, order=order, continuation=continuation, limit=limit, assets=assets)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_txs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} |
 **order** | **str**| Pagination order | [optional]
 **continuation** | **str**| Continuation token from earlier response | [optional]
 **limit** | **int**| Max number of items to return in a response. Defaults to 25 and is capped at 100.  | [optional]
 **assets** | **str**| Comma-separated list of asset paths to filter. If the list is empty, or all elements are empty, this filter has no effect. | [optional]

### Return type

[**TxPage**](TxPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transactions |  -  |
**400** | Invalid address |  -  |
**401** | Invalid or expired token |  -  |
**403** | Invalid continuation |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tx_send**
> TxReceipt tx_send(platform, network, signed_tx)

Submit a signed transaction

Submit a signed transaction to the network.  **Note**: A successful transaction may still be rejected on chain or not processed due to a too low fee. You can monitor successful transactions through Ubiquity websockets. 

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import transactions_api
from ubiquity.ubiquity_openapi_client.model.signed_tx import SignedTx
from ubiquity.ubiquity_openapi_client.model.tx_receipt import TxReceipt
from ubiquity.ubiquity_openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://ubiquity.api.blockdaemon.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    host = "https://ubiquity.api.blockdaemon.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ubiquity.ubiquity_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    platform = "bitcoin" # str | Coin platform handle
    network = "mainnet" # str | Which network to target. Available networks can be found with /{platform}
    signed_tx = SignedTx(
        tx="0100000001ca19af5fb94ced7e62b623d0039a398a42e60050405a1341efe475894629c131010000008b483045022100d77b002b3142013b3f825a730f5bc3ead2014266f07ba4449269af0cf6f086310220365bca1d616ba86fac42ad69efd5f92c5ed6cf16f27ebf5ab55010efc72c219d014104417eb0abe69db2eca63c84eb44266c29c24973dc81cde16ca86c9d923630cb5f797bae7d7fab13498e06146111356eb271da74add05ebda8f72ff2b2878fddb7ffffffff0410270000000000001976a914344a0f48ca150ec2b903817660b9b68b13a6702688ac204e0000000000001976a914344a0f48ca150ec2b903817660b9b68b13a6702688ac30750000000000001976a914344a0f48ca150ec2b903817660b9b68b13a6702688ac48710000000000001976a914d6fa8814924b480fa7ff903b5ef61100ab4d92fe88ac00000000",
    ) # SignedTx | 

    # example passing only required values which don't have defaults set
    try:
        # Submit a signed transaction
        api_response = api_instance.tx_send(platform, network, signed_tx)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->tx_send: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} |
 **signed_tx** | [**SignedTx**](SignedTx.md)|  |

### Return type

[**TxReceipt**](TxReceipt.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A submitted Transaction ID |  -  |
**401** | Invalid or expired token |  -  |
**429** | Rate limit exceeded |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

