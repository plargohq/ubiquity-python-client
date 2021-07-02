"""
    Ubiquity REST API

    Ubiquity provides a RESTful and uniform way to access blockchain resources, with a rich and reusable model across multiple cryptocurrencies.  [Documentation](https://app.blockdaemon.com/docs/ubiquity)  ### Protocols #### Mainnet The following protocols are currently supported: * bitcoin * ethereum * polkadot * xrp * algorand * stellar * dogecoin  #### Testnet * bitcoin/testnet * ethereum/ropsten * dogecoin/testnet  ##### Pagination Certain resources contain a lot of data, more than what's practical to return for a single request. With the help of pagination, the data is split across multiple responses. Each response returns a subset of the items requested and a continuation token.  To get the next batch of items, copy the returned continuation token to the continuation query parameter and repeat the request with the new URL. In case no continuation token is returned, there is no more data available.   # noqa: E501

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
from ubiquity.ubiquity_openapi_client.model.balances_map import BalancesMap
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

        def __get_balances_by_address(
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['platform'] = \
                platform
            kwargs['network'] = \
                network
            kwargs['address'] = \
                address
            return self.call_with_http_info(**kwargs)

        self.get_balances_by_address = _Endpoint(
            settings={
                'response_type': (BalancesMap,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/{platform}/{network}/account/{address}',
                'operation_id': 'get_balances_by_address',
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
            api_client=api_client,
            callable=__get_balances_by_address
        )

        def __get_report_by_address(
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['platform'] = \
                platform
            kwargs['network'] = \
                network
            kwargs['address'] = \
                address
            return self.call_with_http_info(**kwargs)

        self.get_report_by_address = _Endpoint(
            settings={
                'response_type': (Report,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/{platform}/{network}/account/{address}/report',
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
            api_client=api_client,
            callable=__get_report_by_address
        )

        def __get_txs_by_address(
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['platform'] = \
                platform
            kwargs['network'] = \
                network
            kwargs['address'] = \
                address
            return self.call_with_http_info(**kwargs)

        self.get_txs_by_address = _Endpoint(
            settings={
                'response_type': (TxPage,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/{platform}/{network}/account/{address}/txs',
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
                },
                'attribute_map': {
                    'platform': 'platform',
                    'network': 'network',
                    'address': 'address',
                    'order': 'order',
                    'continuation': 'continuation',
                    'limit': 'limit',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
                    'address': 'path',
                    'order': 'query',
                    'continuation': 'query',
                    'limit': 'query',
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
            api_client=api_client,
            callable=__get_txs_by_address
        )
