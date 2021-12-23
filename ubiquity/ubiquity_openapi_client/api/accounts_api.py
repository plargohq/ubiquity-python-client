"""
    Ubiquity REST API

    Ubiquity provides a RESTful and uniform way to access blockchain resources, with a rich and reusable model across multiple cryptocurrencies.  [Documentation](https://app.blockdaemon.com/docs/ubiquity)  ### Protocols #### Mainnet The following protocols are currently supported: * bitcoin * ethereum * polkadot * xrp * algorand * stellar * dogecoin * oasis * stacks * near  #### Testnet * bitcoin/testnet * ethereum/ropsten * dogecoin/testnet  #### Native Ubiquity provides native access to all Blockchain nodes it supports. To access native functionality, use the protocol without the v2 prefix * bitcoin/(mainnet | testnet) - [RPC Documentation](https://developer.bitcoin.org/reference/rpc/) * ethereum/(mainnet | ropsten) - [RPC Documentation](https://ethereum.org/en/developers/docs/apis/json-rpc/) * polkadot/mainnet - [Sidecar API Documentation](https://paritytech.github.io/substrate-api-sidecar/dist/) * polkadot/mainnet/http-rpc - [Polkadot RPC Documentation](https://polkadot.js.org/docs/substrate/rpc/) * algorand/mainnet - [Algod API Documentation](https://developer.algorand.org/docs/reference/rest-apis/algod/v1/) * stellar/mainnet - [Stellar Horizon API Documentation](https://developers.stellar.org/api) * dogecoin/(mainnet | testnet) - [Dogecoin API Documentaion](https://developer.bitcoin.org/reference/rpc/) * oasis/mainnet - [Oasis Rosetta Gateway Documentation](https://www.rosetta-api.org/docs/api_identifiers.html#network-identifier) * stacks/mainnet - [Stacks API Documentation](https://blockstack.github.io/stacks-blockchain-api/) * near/mainnet - [NEAR RPC Documentation](https://docs.near.org/docs/api/rpc)  A full URL example: https://ubiquity.api.blockdaemon.com/bitcoin/mainnet  ##### Pagination Certain resources contain a lot of data, more than what's practical to return for a single request. With the help of pagination, the data is split across multiple responses. Each response returns a subset of the items requested, and a continuation token.  To get the next batch of items, copy the returned continuation token to the continuation query parameter and repeat the request with the new URL. In case no continuation token is returned, there is no more data available.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@blockdaemon.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ubiquity.ubiquity_openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from ubiquity.ubiquity_openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ubiquity.ubiquity_openapi_client.model.accounts_balances_map import AccountsBalancesMap
from ubiquity.ubiquity_openapi_client.model.accounts_balances_map_v1 import AccountsBalancesMapV1
from ubiquity.ubiquity_openapi_client.model.accounts_obj import AccountsObj
from ubiquity.ubiquity_openapi_client.model.balances_map import BalancesMap
from ubiquity.ubiquity_openapi_client.model.balances_map_v1 import BalancesMapV1
from ubiquity.ubiquity_openapi_client.model.error import Error
from ubiquity.ubiquity_openapi_client.model.report import Report
from ubiquity.ubiquity_openapi_client.model.tx_page import TxPage


class AccountsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_balances_by_address_endpoint = _Endpoint(
            settings={
                'response_type': (BalancesMap,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v2/{platform}/{network}/account/{address}',
                'operation_id': 'get_balances_by_address',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'platform',
                    'network',
                    'address',
                    'assets',
                ],
                'required': [
                    'platform',
                    'network',
                    'address',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'platform':
                        (str,),
                    'network':
                        (str,),
                    'address':
                        (str,),
                    'assets':
                        (str,),
                },
                'attribute_map': {
                    'platform': 'platform',
                    'network': 'network',
                    'address': 'address',
                    'assets': 'assets',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
                    'address': 'path',
                    'assets': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_balances_by_addresses_endpoint = _Endpoint(
            settings={
                'response_type': (AccountsBalancesMap,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v2/{platform}/{network}/accounts',
                'operation_id': 'get_balances_by_addresses',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'platform',
                    'network',
                    'accounts_obj',
                    'assets',
                ],
                'required': [
                    'platform',
                    'network',
                    'accounts_obj',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'platform':
                        (str,),
                    'network':
                        (str,),
                    'accounts_obj':
                        (AccountsObj,),
                    'assets':
                        (str,),
                },
                'attribute_map': {
                    'platform': 'platform',
                    'network': 'network',
                    'assets': 'assets',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
                    'accounts_obj': 'body',
                    'assets': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_list_of_balances_by_address_endpoint = _Endpoint(
            settings={
                'response_type': (BalancesMapV1,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v1/{platform}/{network}/account/{address}',
                'operation_id': 'get_list_of_balances_by_address',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'platform',
                    'network',
                    'address',
                ],
                'required': [
                    'platform',
                    'network',
                    'address',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'platform':
                        (str,),
                    'network':
                        (str,),
                    'address':
                        (str,),
                },
                'attribute_map': {
                    'platform': 'platform',
                    'network': 'network',
                    'address': 'address',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
                    'address': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_list_of_balances_by_addresses_endpoint = _Endpoint(
            settings={
                'response_type': (AccountsBalancesMapV1,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v1/{platform}/{network}/accounts',
                'operation_id': 'get_list_of_balances_by_addresses',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'platform',
                    'network',
                    'accounts_obj',
                ],
                'required': [
                    'platform',
                    'network',
                    'accounts_obj',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'platform':
                        (str,),
                    'network':
                        (str,),
                    'accounts_obj':
                        (AccountsObj,),
                },
                'attribute_map': {
                    'platform': 'platform',
                    'network': 'network',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
                    'accounts_obj': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_report_by_address_endpoint = _Endpoint(
            settings={
                'response_type': (Report,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v2/{platform}/{network}/account/{address}/report',
                'operation_id': 'get_report_by_address',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'platform',
                    'network',
                    'address',
                    '_from',
                    'to',
                ],
                'required': [
                    'platform',
                    'network',
                    'address',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'platform':
                        (str,),
                    'network':
                        (str,),
                    'address':
                        (str,),
                    '_from':
                        (int,),
                    'to':
                        (int,),
                },
                'attribute_map': {
                    'platform': 'platform',
                    'network': 'network',
                    'address': 'address',
                    '_from': 'from',
                    'to': 'to',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
                    'address': 'path',
                    '_from': 'query',
                    'to': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/csv',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_txs_by_address_endpoint = _Endpoint(
            settings={
                'response_type': (TxPage,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v2/{platform}/{network}/account/{address}/txs',
                'operation_id': 'get_txs_by_address',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'platform',
                    'network',
                    'address',
                    'order',
                    'continuation',
                    'limit',
                    'assets',
                ],
                'required': [
                    'platform',
                    'network',
                    'address',
                ],
                'nullable': [
                ],
                'enum': [
                    'order',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('order',): {

                        "DESC": "desc",
                        "ASC": "asc"
                    },
                },
                'openapi_types': {
                    'platform':
                        (str,),
                    'network':
                        (str,),
                    'address':
                        (str,),
                    'order':
                        (str,),
                    'continuation':
                        (str,),
                    'limit':
                        (int,),
                    'assets':
                        (str,),
                },
                'attribute_map': {
                    'platform': 'platform',
                    'network': 'network',
                    'address': 'address',
                    'order': 'order',
                    'continuation': 'continuation',
                    'limit': 'limit',
                    'assets': 'assets',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
                    'address': 'path',
                    'order': 'query',
                    'continuation': 'query',
                    'limit': 'query',
                    'assets': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_balances_by_address(
        self,
        platform,
        network,
        address,
        **kwargs
    ):
        """Balances Of Address  # noqa: E501

        Returns the account balances for all supported currencies.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_balances_by_address(platform, network, address, async_req=True)
        >>> result = thread.get()

        Args:
            platform (str): Coin platform handle
            network (str): Which network to target. Available networks can be found with /{platform}
            address (str): Account address

        Keyword Args:
            assets (str): Comma-separated list of asset paths to filter. If the list is empty, or all elements are empty, this filter has no effect.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BalancesMap
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['platform'] = \
            platform
        kwargs['network'] = \
            network
        kwargs['address'] = \
            address
        return self.get_balances_by_address_endpoint.call_with_http_info(**kwargs)

    def get_balances_by_addresses(
        self,
        platform,
        network,
        accounts_obj,
        **kwargs
    ):
        """Balances Of Addresses  # noqa: E501

        Returns the balances of accounts for all supported currencies.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_balances_by_addresses(platform, network, accounts_obj, async_req=True)
        >>> result = thread.get()

        Args:
            platform (str): Coin platform handle
            network (str): Which network to target. Available networks can be found with /{platform}
            accounts_obj (AccountsObj):

        Keyword Args:
            assets (str): Comma-separated list of asset paths to filter. If the list is empty, or all elements are empty, this filter has no effect.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AccountsBalancesMap
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['platform'] = \
            platform
        kwargs['network'] = \
            network
        kwargs['accounts_obj'] = \
            accounts_obj
        return self.get_balances_by_addresses_endpoint.call_with_http_info(**kwargs)

    def get_list_of_balances_by_address(
        self,
        platform,
        network,
        address,
        **kwargs
    ):
        """Balances Of Address  # noqa: E501

        Returns the account balances for all supported currencies.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_list_of_balances_by_address(platform, network, address, async_req=True)
        >>> result = thread.get()

        Args:
            platform (str): Coin platform handle
            network (str): Which network to target. Available networks can be found with /{platform}
            address (str): Account address

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            BalancesMapV1
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['platform'] = \
            platform
        kwargs['network'] = \
            network
        kwargs['address'] = \
            address
        return self.get_list_of_balances_by_address_endpoint.call_with_http_info(**kwargs)

    def get_list_of_balances_by_addresses(
        self,
        platform,
        network,
        accounts_obj,
        **kwargs
    ):
        """Balances Of Addresses  # noqa: E501

        Returns the balances of accounts for all supported currencies.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_list_of_balances_by_addresses(platform, network, accounts_obj, async_req=True)
        >>> result = thread.get()

        Args:
            platform (str): Coin platform handle
            network (str): Which network to target. Available networks can be found with /{platform}
            accounts_obj (AccountsObj):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AccountsBalancesMapV1
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['platform'] = \
            platform
        kwargs['network'] = \
            network
        kwargs['accounts_obj'] = \
            accounts_obj
        return self.get_list_of_balances_by_addresses_endpoint.call_with_http_info(**kwargs)

    def get_report_by_address(
        self,
        platform,
        network,
        address,
        **kwargs
    ):
        """A financial report for an address between a time period. Default timescale is within the last 30 days  # noqa: E501

        Returns account activity   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_report_by_address(platform, network, address, async_req=True)
        >>> result = thread.get()

        Args:
            platform (str): Coin platform handle
            network (str): Which network to target. Available networks can be found with /{platform}
            address (str): Account address

        Keyword Args:
            _from (int): Unix Timestamp from where to start. [optional]
            to (int): Unix Timestamp from where to end. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Report
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['platform'] = \
            platform
        kwargs['network'] = \
            network
        kwargs['address'] = \
            address
        return self.get_report_by_address_endpoint.call_with_http_info(**kwargs)

    def get_txs_by_address(
        self,
        platform,
        network,
        address,
        **kwargs
    ):
        """Transactions Of Address  # noqa: E501

        Gets transactions that an address was involved with, from newest to oldest. This call uses pagination.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_txs_by_address(platform, network, address, async_req=True)
        >>> result = thread.get()

        Args:
            platform (str): Coin platform handle
            network (str): Which network to target. Available networks can be found with /{platform}
            address (str): Account address

        Keyword Args:
            order (str): Pagination order. [optional]
            continuation (str): Continuation token from earlier response. [optional]
            limit (int): Max number of items to return in a response. Defaults to 25 and is capped at 100. . [optional]
            assets (str): Comma-separated list of asset paths to filter. If the list is empty, or all elements are empty, this filter has no effect.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TxPage
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['platform'] = \
            platform
        kwargs['network'] = \
            network
        kwargs['address'] = \
            address
        return self.get_txs_by_address_endpoint.call_with_http_info(**kwargs)

