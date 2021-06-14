# ubiquity.ubiquity_openapi_client.PlatformsApi

All URIs are relative to *https://ubiquity.api.blockdaemon.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_platform**](PlatformsApi.md#get_platform) | **GET** /{platform}/{network} | Platform Info


# **get_platform**
> PlatformDetail get_platform(platform, )

Platform Info

Provides information about supported endpoints and generic platform information. 

### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import platforms_api
from ubiquity.ubiquity_openapi_client.model.platform_detail import PlatformDetail
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
    api_instance = platforms_api.PlatformsApi(api_client)
    platform = "ethereum" # str | Coin platform handle

    # example passing only required values which don't have defaults set
    try:
        # Platform Info
        api_response = api_instance.get_platform(platform, )
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling PlatformsApi->get_platform: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform** | **str**| Coin platform handle |
 **network** | **str**| Which network to target. Available networks can be found with /{platform} | defaults to "mainnet"

### Return type

[**PlatformDetail**](PlatformDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Platform overview |  -  |
**401** | Invalid or expired token |  -  |
**429** | Rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

