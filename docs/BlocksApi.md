# ubiquity.ubiquity_openapi_client.BlocksApi

All URIs are relative to *https://ubiquity.api.blockdaemon.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_block**](BlocksApi.md#get_block) | **GET** /{platform}/{network}/block/{key} | Block By Number/Hash
[**get_block_identifier**](BlocksApi.md#get_block_identifier) | **GET** /{platform}/{network}/block_identifier/{key} | Block Identifier By Number/Hash


# **get_block**
> Block get_block(platform, key)

Block By Number/Hash

Get a block and all its transactions by the block number or hash

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import blocks_api
from ubiquity.ubiquity_openapi_client.model.block import Block
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
    api_instance = blocks_api.BlocksApi(api_client)
    platform = "ethereum" # str | Coin platform handle
    key = "8000000" # str | Block number or block hash/ID or Special identifier

    # example passing only required values which don't have defaults set
    try:
        # Block By Number/Hash
        api_response = api_instance.get_block(platform, key)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling BlocksApi->get_block: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **key** | **str**| Block number or block hash/ID or Special identifier |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} | defaults to "mainnet"

### Return type

[**Block**](Block.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Block |  -  |
**400** | Invalid Block Number |  -  |
**401** | Invalid or expired token |  -  |
**404** | Not Found |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_identifier**
> BlockIdentifier get_block_identifier(platform, key)

Block Identifier By Number/Hash

Get minimal block identifier by block number or hash

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import blocks_api
from ubiquity.ubiquity_openapi_client.model.error import Error
from ubiquity.ubiquity_openapi_client.model.block_identifier import BlockIdentifier
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
    api_instance = blocks_api.BlocksApi(api_client)
    platform = "ethereum" # str | Coin platform handle
    key = "8000000" # str | Block number or block hash/ID or Special identifier

    # example passing only required values which don't have defaults set
    try:
        # Block Identifier By Number/Hash
        api_response = api_instance.get_block_identifier(platform, key)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling BlocksApi->get_block_identifier: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **key** | **str**| Block number or block hash/ID or Special identifier |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} | defaults to "mainnet"

### Return type

[**BlockIdentifier**](BlockIdentifier.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Block |  -  |
**400** | Invalid Block Number |  -  |
**401** | Invalid or expired token |  -  |
**404** | Not Found |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

