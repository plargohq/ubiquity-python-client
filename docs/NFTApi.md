# ubiquity.ubiquity_openapi_client.NFTApi

All URIs are relative to *https://ubiquity.api.blockdaemon.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**explorer_get_collection**](NFTApi.md#explorer_get_collection) | **GET** /nft/{protocol}/{network}/collection/{id} | 
[**explorer_list_assets**](NFTApi.md#explorer_list_assets) | **GET** /nft/{protocol}/{network}/assets | 
[**explorer_list_collections**](NFTApi.md#explorer_list_collections) | **GET** /nft/{protocol}/{network}/collections | 
[**explorer_list_events**](NFTApi.md#explorer_list_events) | **GET** /nft/{protocol}/{network}/events | 


# **explorer_get_collection**
> GetCollectionResponse explorer_get_collection(protocol, network, id)



### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import nft_api
from ubiquity.ubiquity_openapi_client.model.get_collection_response import GetCollectionResponse
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
    api_instance = nft_api.NFTApi(api_client)
    protocol = "protocol_example" # str | Coin platform handle
    network = "network_example" # str | Which network to target
    id = "id_example" # str | Mapped to URL query parameter 'uuid'

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.explorer_get_collection(protocol, network, id)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling NFTApi->explorer_get_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol** | **str**| Coin platform handle |
 **network** | **str**| Which network to target |
 **id** | **str**| Mapped to URL query parameter &#39;uuid&#39; |

### Return type

[**GetCollectionResponse**](GetCollectionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explorer_list_assets**
> ListAssetsResponse explorer_list_assets(protocol, network)



### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import nft_api
from ubiquity.ubiquity_openapi_client.model.list_assets_response import ListAssetsResponse
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
    api_instance = nft_api.NFTApi(api_client)
    protocol = "protocol_example" # str | Coin platform handle
    network = "network_example" # str | Which network to target
    wallet_address = "wallet_address_example" # str | Mapped to URL query parameter `wallet_address` (optional)
    contract_address = "contract_address_example" # str | Mapped to URL query parameter `contract_address` (optional)
    token_id_value = 1 # int | The int64 value. (optional)
    collection_name = "collection_name_example" # str | Mapped to URL query parameter `collection_name` (optional)
    sort_by = "sort_by_example" # str | One of: name, token_id, mint_date (optional)
    order = "order_example" # str | Mapped to URL query parameter `order` One of: asc, desc (optional)
    page_size = 1 # int | Mapped to URL query parameter `page_size` (optional)
    page_token = "page_token_example" # str | Mapped to URL query parameter `page_token` base64 encoded cursor (optional)
    attributes = [
        "attributes_example",
    ] # [str] | Mapped to URL query parameter `attributes` (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.explorer_list_assets(protocol, network)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling NFTApi->explorer_list_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.explorer_list_assets(protocol, network, wallet_address=wallet_address, contract_address=contract_address, token_id_value=token_id_value, collection_name=collection_name, sort_by=sort_by, order=order, page_size=page_size, page_token=page_token, attributes=attributes)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling NFTApi->explorer_list_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol** | **str**| Coin platform handle |
 **network** | **str**| Which network to target |
 **wallet_address** | **str**| Mapped to URL query parameter &#x60;wallet_address&#x60; | [optional]
 **contract_address** | **str**| Mapped to URL query parameter &#x60;contract_address&#x60; | [optional]
 **token_id_value** | **int**| The int64 value. | [optional]
 **collection_name** | **str**| Mapped to URL query parameter &#x60;collection_name&#x60; | [optional]
 **sort_by** | **str**| One of: name, token_id, mint_date | [optional]
 **order** | **str**| Mapped to URL query parameter &#x60;order&#x60; One of: asc, desc | [optional]
 **page_size** | **int**| Mapped to URL query parameter &#x60;page_size&#x60; | [optional]
 **page_token** | **str**| Mapped to URL query parameter &#x60;page_token&#x60; base64 encoded cursor | [optional]
 **attributes** | **[str]**| Mapped to URL query parameter &#x60;attributes&#x60; | [optional]

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explorer_list_collections**
> ListCollectionResponse explorer_list_collections(protocol, network)



### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import nft_api
from ubiquity.ubiquity_openapi_client.model.list_collection_response import ListCollectionResponse
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
    api_instance = nft_api.NFTApi(api_client)
    protocol = "protocol_example" # str | Coin platform handle
    network = "network_example" # str | Which network to target
    contract_address = [
        "contractAddress_example",
    ] # [str] | Mapped to URL query parameter 'contract_address' (optional)
    collection_name = [
        "collectionName_example",
    ] # [str] | Mapped to URL query parameter 'collection_name' (optional)
    sort_by = "sort_by_example" # str | Sort by one of: name (optional)
    order = "order_example" # str | Mapped to URL query parameter `order` One of: asc, desc (optional)
    page_size = 1 # int | Mapped to URL query parameter `page_size` (optional)
    page_token = "page_token_example" # str | Mapped to URL query parameter `page_token` base64 encoded cursor (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.explorer_list_collections(protocol, network)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling NFTApi->explorer_list_collections: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.explorer_list_collections(protocol, network, contract_address=contract_address, collection_name=collection_name, sort_by=sort_by, order=order, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling NFTApi->explorer_list_collections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol** | **str**| Coin platform handle |
 **network** | **str**| Which network to target |
 **contract_address** | **[str]**| Mapped to URL query parameter &#39;contract_address&#39; | [optional]
 **collection_name** | **[str]**| Mapped to URL query parameter &#39;collection_name&#39; | [optional]
 **sort_by** | **str**| Sort by one of: name | [optional]
 **order** | **str**| Mapped to URL query parameter &#x60;order&#x60; One of: asc, desc | [optional]
 **page_size** | **int**| Mapped to URL query parameter &#x60;page_size&#x60; | [optional]
 **page_token** | **str**| Mapped to URL query parameter &#x60;page_token&#x60; base64 encoded cursor | [optional]

### Return type

[**ListCollectionResponse**](ListCollectionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explorer_list_events**
> ListEventResponse explorer_list_events(protocol, network)



### Example

* Bearer (Opaque) Authentication (bearerAuth):
```python
import time
import ubiquity.ubiquity_openapi_client
from ubiquity.ubiquity_openapi_client.api import nft_api
from ubiquity.ubiquity_openapi_client.model.list_event_response import ListEventResponse
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
    api_instance = nft_api.NFTApi(api_client)
    protocol = "protocol_example" # str | Coin platform handle
    network = "network_example" # str | Which network to target
    contract_address = "contract_address_example" # str | mapped to URL query parameter 'contract_address' (optional)
    wallet_address = "wallet_address_example" # str | mapped to URL query parameter 'wallet_address' (optional)
    token_id = 1 # int | mapped to URL query parameter 'token_id' (optional)
    event_type = "event_type_example" # str | mapped to URL query parameter 'event_type' (optional)
    sort_by = "sort_by_example" # str | Sort by one of: timestamp (optional)
    order = "order_example" # str | Mapped to URL query parameter `order` One of: asc, desc (optional)
    page_size = 1 # int | Mapped to URL query parameter `page_size` (optional)
    page_token = "page_token_example" # str | Mapped to URL query parameter `page_token` base64 encoded cursor (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.explorer_list_events(protocol, network)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling NFTApi->explorer_list_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.explorer_list_events(protocol, network, contract_address=contract_address, wallet_address=wallet_address, token_id=token_id, event_type=event_type, sort_by=sort_by, order=order, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except ubiquity.ubiquity_openapi_client.ApiException as e:
        print("Exception when calling NFTApi->explorer_list_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol** | **str**| Coin platform handle |
 **network** | **str**| Which network to target |
 **contract_address** | **str**| mapped to URL query parameter &#39;contract_address&#39; | [optional]
 **wallet_address** | **str**| mapped to URL query parameter &#39;wallet_address&#39; | [optional]
 **token_id** | **int**| mapped to URL query parameter &#39;token_id&#39; | [optional]
 **event_type** | **str**| mapped to URL query parameter &#39;event_type&#39; | [optional]
 **sort_by** | **str**| Sort by one of: timestamp | [optional]
 **order** | **str**| Mapped to URL query parameter &#x60;order&#x60; One of: asc, desc | [optional]
 **page_size** | **int**| Mapped to URL query parameter &#x60;page_size&#x60; | [optional]
 **page_token** | **str**| Mapped to URL query parameter &#x60;page_token&#x60; base64 encoded cursor | [optional]

### Return type

[**ListEventResponse**](ListEventResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

