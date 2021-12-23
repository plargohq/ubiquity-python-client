# ubiquity.ubiquity_openapi_client.SyncApi

All URIs are relative to *https://ubiquity.api.blockdaemon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**current_block_id**](SyncApi.md#current_block_id) | **GET** /v2/{platform}/{network}/sync/block_id | Get current block ID
[**current_block_number**](SyncApi.md#current_block_number) | **GET** /v2/{platform}/{network}/sync/block_number | Get current block number


# **current_block_id**
> str current_block_id(platform, network)

Get current block ID

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import sync_api
from ubiquity.ubiquity_openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://ubiquity.api.blockdaemon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    host = "https://ubiquity.api.blockdaemon.com"
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
    api_instance = sync_api.SyncApi(api_client)
    platform = "bitcoin" # str | Coin platform handle
    network = "mainnet" # str | Which network to target. Available networks can be found with /{platform}

    # example passing only required values which don't have defaults set
    try:
        # Get current block ID
        api_response = api_instance.current_block_id(platform, network)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling SyncApi->current_block_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} |

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current block ID |  -  |
**401** | Invalid or expired token |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **current_block_number**
> int current_block_number(platform, network)

Get current block number

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import sync_api
from ubiquity.ubiquity_openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://ubiquity.api.blockdaemon.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ubiquity.ubiquity_openapi_client.Configuration(
    host = "https://ubiquity.api.blockdaemon.com"
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
    api_instance = sync_api.SyncApi(api_client)
    platform = "bitcoin" # str | Coin platform handle
    network = "mainnet" # str | Which network to target. Available networks can be found with /{platform}

    # example passing only required values which don't have defaults set
    try:
        # Get current block number
        api_response = api_instance.current_block_number(platform, network)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling SyncApi->current_block_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} |

### Return type

**int**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current block number |  -  |
**401** | Invalid or expired token |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

