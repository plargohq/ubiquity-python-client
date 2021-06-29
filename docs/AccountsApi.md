# ubiquity.ubiquity_openapi_client.AccountsApi

All URIs are relative to *https://ubiquity.api.blockdaemon.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balances_by_address**](AccountsApi.md#get_balances_by_address) | **GET** /{platform}/{network}/account/{address} | Balances Of Address
[**get_report_by_address**](AccountsApi.md#get_report_by_address) | **GET** /{platform}/{network}/account/{address}/report | A financial report for an address between a time period. Default timescale is within the last 30 days
[**get_txs_by_address**](AccountsApi.md#get_txs_by_address) | **GET** /{platform}/{network}/account/{address}/txs | Transactions Of Address


# **get_balances_by_address**
> BalancesMap get_balances_by_address(platform, network, address)

Balances Of Address

Returns the account balances for all supported currencies. 

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import accounts_api
from ubiquity.ubiquity_openapi_client.model.error import Error
from ubiquity.ubiquity_openapi_client.model.balances_map import BalancesMap
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
    api_instance = accounts_api.AccountsApi(api_client)
    platform = "bitcoin" # str | Coin platform handle
    network = "mainnet" # str | Which network to target. Available networks can be found with /{platform}
    address = "0x2E31B312290A01538514806Fbb857736ea4d5555" # str | Account address

    # example passing only required values which don't have defaults set
    try:
        # Balances Of Address
        api_response = api_instance.get_balances_by_address(platform, network, address)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling AccountsApi->get_balances_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} |
 **address** | **str**| Account address |

### Return type

[**BalancesMap**](BalancesMap.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Balances |  -  |
**400** | Bad request |  -  |
**401** | Invalid or expired token |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_by_address**
> Report get_report_by_address(platform, network, address)

A financial report for an address between a time period. Default timescale is within the last 30 days

Returns account activity 

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import accounts_api
from ubiquity.ubiquity_openapi_client.model.error import Error
from ubiquity.ubiquity_openapi_client.model.report import Report
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
    api_instance = accounts_api.AccountsApi(api_client)
    platform = "bitcoin" # str | Coin platform handle
    network = "mainnet" # str | Which network to target. Available networks can be found with /{platform}
    address = "0x2E31B312290A01538514806Fbb857736ea4d5555" # str | Account address
    _from = 961846434 # int | Unix Timestamp from where to start (optional)
    to = 1119612834 # int | Unix Timestamp from where to end (optional)

    # example passing only required values which don't have defaults set
    try:
        # A financial report for an address between a time period. Default timescale is within the last 30 days
        api_response = api_instance.get_report_by_address(platform, network, address)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling AccountsApi->get_report_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # A financial report for an address between a time period. Default timescale is within the last 30 days
        api_response = api_instance.get_report_by_address(platform, network, address, _from=_from, to=to)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling AccountsApi->get_report_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} |
 **address** | **str**| Account address |
 **_from** | **int**| Unix Timestamp from where to start | [optional]
 **to** | **int**| Unix Timestamp from where to end | [optional]

### Return type

[**Report**](Report.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/problem+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account Activity |  -  |
**400** | Bad request |  -  |
**401** | Invalid or expired token |  -  |
**429** | Rate limit exceeded |  -  |
**413** | Too Many Transactions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_txs_by_address**
> TxPage get_txs_by_address(platform, network, address)

Transactions Of Address

Gets transactions that an address was involved with, from newest to oldest. This call uses pagination. 

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import accounts_api
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
    api_instance = accounts_api.AccountsApi(api_client)
    platform = "bitcoin" # str | Coin platform handle
    network = "mainnet" # str | Which network to target. Available networks can be found with /{platform}
    address = "0x2E31B312290A01538514806Fbb857736ea4d5555" # str | Account address
    order = "desc" # str | Pagination order (optional)
    continuation = "8185.123" # str | Continuation token from earlier response (optional)
    limit = 25 # int | Max number of items to return in a response. Defaults to 25 and is capped at 100.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Transactions Of Address
        api_response = api_instance.get_txs_by_address(platform, network, address)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling AccountsApi->get_txs_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Transactions Of Address
        api_response = api_instance.get_txs_by_address(platform, network, address, order=order, continuation=continuation, limit=limit)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling AccountsApi->get_txs_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} |
 **address** | **str**| Account address |
 **order** | **str**| Pagination order | [optional]
 **continuation** | **str**| Continuation token from earlier response | [optional]
 **limit** | **int**| Max number of items to return in a response. Defaults to 25 and is capped at 100.  | [optional]

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

