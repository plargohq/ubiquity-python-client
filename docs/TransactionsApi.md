# ubiquity.ubiquity_openapi_client.TransactionsApi

All URIs are relative to *https://ubiquity.api.blockdaemon.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tx**](TransactionsApi.md#get_tx) | **GET** /{platform}/{network}/tx/{id} | Transaction By Hash
[**get_txs**](TransactionsApi.md#get_txs) | **GET** /{platform}/{network}/txs | All Transactions


# **get_tx**
> Tx get_tx(platform, id)

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
# Defining the host is optional and defaults to https://ubiquity.api.blockdaemon.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    host = "https://ubiquity.api.blockdaemon.com/v2"
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
    platform = "ethereum" # str | Coin platform handle
    id = "0xF00Fa860473130C1df10707223E66Cb4B839B165" # str | Transaction ID/Hash

    # example passing only required values which don't have defaults set
    try:
        # Transaction By Hash
        api_response = api_instance.get_tx(platform, id)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_tx: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **id** | **str**| Transaction ID/Hash |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} | defaults to "mainnet"

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

# **get_txs**
> TxPage get_txs(platform, )

All Transactions

Get all transactions on the platform, starting with the lastest one. Each call returns a slice of the entire list. Use the returned continuation token to get the next part.

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import transactions_api
from ubiquity.ubiquity_openapi_client.model.error import Error
from ubiquity.ubiquity_openapi_client.model.tx_page import TxPage
from pprint import pprint
# Defining the host is optional and defaults to https://ubiquity.api.blockdaemon.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    host = "https://ubiquity.api.blockdaemon.com/v2"
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
    platform = "ethereum" # str | Coin platform handle
    order = "desc" # str | Pagination order (optional)
    continuation = "8185.123" # str | Continuation token from earlier response (optional)
    limit = 25 # int | Max number of items to return in a response. Defaults to 25 and is capped at 100.  (optional)
    assets = "ethereum/native/eth:ethereum/currency2" # str | Comma-separated list of asset paths to filter. If the list is empty, or all elements are empty, this filter has no effect. (optional)

    # example passing only required values which don't have defaults set
    try:
        # All Transactions
        api_response = api_instance.get_txs(platform, )
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_txs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # All Transactions
        api_response = api_instance.get_txs(platform, order=order, continuation=continuation, limit=limit, assets=assets)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_txs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} | defaults to "mainnet"
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
**401** | Invalid or expired token |  -  |
**403** | Invalid continuation |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

