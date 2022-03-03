"""
    Ubiquity REST API

    Ubiquity provides a RESTful and uniform way to access blockchain resources, with a rich and reusable model across multiple cryptocurrencies.  [Documentation](https://app.blockdaemon.com/docs/ubiquity)  ### Protocols #### Mainnet The following protocols are currently supported: * bitcoin * ethereum * polkadot * xrp * algorand * stellar * dogecoin * oasis * near * terra * litecoin * bitcoincash  #### Testnet * bitcoin/testnet * ethereum/ropsten * dogecoin/testnet * litecoin/testnet * bitcoincash/testnet  #### Native Ubiquity provides native access to all Blockchain nodes it supports. To access native functionality, use the protocol without the v2 prefix * bitcoin/(mainnet | testnet) - [RPC Documentation](https://developer.bitcoin.org/reference/rpc/) * ethereum/(mainnet | ropsten) - [RPC Documentation](https://ethereum.org/en/developers/docs/apis/json-rpc/) * polkadot/mainnet - [Sidecar API Documentation](https://paritytech.github.io/substrate-api-sidecar/dist/) * polkadot/mainnet/http-rpc - [Polkadot RPC Documentation](https://polkadot.js.org/docs/substrate/rpc/) * algorand/mainnet - [Algod API Documentation](https://developer.algorand.org/docs/reference/rest-apis/algod/v1/) * stellar/mainnet - [Stellar Horizon API Documentation](https://developers.stellar.org/api) * dogecoin/(mainnet | testnet) - [Dogecoin API Documentaion](https://developer.bitcoin.org/reference/rpc/) * oasis/mainnet - [Oasis Rosetta Gateway Documentation](https://www.rosetta-api.org/docs/api_identifiers.html#network-identifier) * near/mainnet - [NEAR RPC Documentation](https://docs.near.org/docs/api/rpc) * terra/mainnet - [Terra RPC Documentation](https://docs.terra.money/docs/develop/how-to/endpoints.html) * litecoin/mainnet - [Litecoin RPC Documentation](https://litecoin.info/index.php/Litecoin_API) * bitcoincash/mainnet - [Bitcoin Cash RPC Documentation](https://docs.bitcoincashnode.org/doc/json-rpc/)  A full URL example: https://ubiquity.api.blockdaemon.com/bitcoin/mainnet  ##### Pagination Certain resources contain a lot of data, more than what's practical to return for a single request. With the help of pagination, the data is split across multiple responses. Each response returns a subset of the items requested, and a continuation token.  To get the next batch of items, copy the returned continuation token to the continuation query parameter and repeat the request with the new URL. In case no continuation token is returned, there is no more data available.   # noqa: E501

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
from ubiquity.ubiquity_openapi_client.model.error import Error
from ubiquity.ubiquity_openapi_client.model.fee_estimate import FeeEstimate
from ubiquity.ubiquity_openapi_client.model.signed_tx import SignedTx
from ubiquity.ubiquity_openapi_client.model.tx import Tx
from ubiquity.ubiquity_openapi_client.model.tx_confirmation import TxConfirmation
from ubiquity.ubiquity_openapi_client.model.tx_page import TxPage
from ubiquity.ubiquity_openapi_client.model.tx_receipt import TxReceipt


class TransactionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __estimate_fee(
            self,
            platform,
            network,
            **kwargs
        ):
            """Get fee estimate  # noqa: E501

            Get a fee estimation in decimals from the network. If supported by the platform, the number of blocks used to make the estimation can be customized by the confirmed_within_blocks query parameter.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.estimate_fee(platform, network, async_req=True)
            >>> result = thread.get()

            Args:
                platform (str): Coin platform handle
                network (str): Which network to target. Available networks can be found with /{platform}

            Keyword Args:
                confirmed_within_blocks (int): The number of blocks you would like the transaction to be processed within. Lower numbers produce higher fees. . [optional] if omitted the server will use the default value of 10
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
                str
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
            return self.call_with_http_info(**kwargs)

        self.estimate_fee = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v2/{platform}/{network}/tx/estimate_fee',
                'operation_id': 'estimate_fee',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'platform',
                    'network',
                    'confirmed_within_blocks',
                ],
                'required': [
                    'platform',
                    'network',
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
                    'confirmed_within_blocks':
                        (int,),
                },
                'attribute_map': {
                    'platform': 'platform',
                    'network': 'network',
                    'confirmed_within_blocks': 'confirmed_within_blocks',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
                    'confirmed_within_blocks': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__estimate_fee
        )

        def __fee_estimate(
            self,
            platform,
            network,
            **kwargs
        ):
            """Get fee estimate  # noqa: E501

            Get a fee estimation in decimals from the ubiquity fee estimation service. Currently supported for Bitcoin and Ethereum. Endpoint will return 3 fee estimations fast, medium and slow   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fee_estimate(platform, network, async_req=True)
            >>> result = thread.get()

            Args:
                platform (str): Coin platform handle
                network (str): Which network to target. Available networks can be found with /{platform}

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
                FeeEstimate
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
            return self.call_with_http_info(**kwargs)

        self.fee_estimate = _Endpoint(
            settings={
                'response_type': (FeeEstimate,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v1/{platform}/{network}/tx/estimate_fee',
                'operation_id': 'fee_estimate',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'platform',
                    'network',
                ],
                'required': [
                    'platform',
                    'network',
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
                },
                'attribute_map': {
                    'platform': 'platform',
                    'network': 'network',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__fee_estimate
        )

        def __get_tx(
            self,
            platform,
            network,
            id,
            **kwargs
        ):
            """Transaction By Hash  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_tx(platform, network, id, async_req=True)
            >>> result = thread.get()

            Args:
                platform (str): Coin platform handle
                network (str): Which network to target. Available networks can be found with /{platform}
                id (str): Transaction ID/Hash

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
                Tx
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
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.get_tx = _Endpoint(
            settings={
                'response_type': (Tx,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v2/{platform}/{network}/tx/{id}',
                'operation_id': 'get_tx',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'platform',
                    'network',
                    'id',
                ],
                'required': [
                    'platform',
                    'network',
                    'id',
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
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'platform': 'platform',
                    'network': 'network',
                    'id': 'id',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
                    'id': 'path',
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
            callable=__get_tx
        )

        def __get_tx_confirmations(
            self,
            platform,
            network,
            id,
            **kwargs
        ):
            """Transaction confirmations By Hash  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_tx_confirmations(platform, network, id, async_req=True)
            >>> result = thread.get()

            Args:
                platform (str): Coin platform handle
                network (str): Which network to target. Available networks can be found with /{platform}
                id (str): Transaction ID/Hash

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
                TxConfirmation
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
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.get_tx_confirmations = _Endpoint(
            settings={
                'response_type': (TxConfirmation,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v1/{platform}/{network}/tx/{id}/confirmations',
                'operation_id': 'get_tx_confirmations',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'platform',
                    'network',
                    'id',
                ],
                'required': [
                    'platform',
                    'network',
                    'id',
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
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'platform': 'platform',
                    'network': 'network',
                    'id': 'id',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
                    'id': 'path',
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
            callable=__get_tx_confirmations
        )

        def __get_txs(
            self,
            platform,
            network,
            **kwargs
        ):
            """All Transactions  # noqa: E501

            Get all transactions on the platform, starting with the lastest one. Each call returns a slice of the entire list. Use the returned continuation token to get the next part.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_txs(platform, network, async_req=True)
            >>> result = thread.get()

            Args:
                platform (str): Coin platform handle
                network (str): Which network to target. Available networks can be found with /{platform}

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
            return self.call_with_http_info(**kwargs)

        self.get_txs = _Endpoint(
            settings={
                'response_type': (TxPage,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v2/{platform}/{network}/txs',
                'operation_id': 'get_txs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'platform',
                    'network',
                    'order',
                    'continuation',
                    'limit',
                    'assets',
                ],
                'required': [
                    'platform',
                    'network',
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
                    'order': 'order',
                    'continuation': 'continuation',
                    'limit': 'limit',
                    'assets': 'assets',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
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
            api_client=api_client,
            callable=__get_txs
        )

        def __tx_send(
            self,
            platform,
            network,
            signed_tx,
            **kwargs
        ):
            """Submit a signed transaction  # noqa: E501

            Submit a signed transaction to the network.  **Note**: A successful transaction may still be rejected on chain or not processed due to a too low fee. You can monitor successful transactions through Ubiquity websockets.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tx_send(platform, network, signed_tx, async_req=True)
            >>> result = thread.get()

            Args:
                platform (str): Coin platform handle
                network (str): Which network to target. Available networks can be found with /{platform}
                signed_tx (SignedTx):

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
                TxReceipt
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
            kwargs['signed_tx'] = \
                signed_tx
            return self.call_with_http_info(**kwargs)

        self.tx_send = _Endpoint(
            settings={
                'response_type': (TxReceipt,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/v2/{platform}/{network}/tx/send',
                'operation_id': 'tx_send',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'platform',
                    'network',
                    'signed_tx',
                ],
                'required': [
                    'platform',
                    'network',
                    'signed_tx',
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
                    'signed_tx':
                        (SignedTx,),
                },
                'attribute_map': {
                    'platform': 'platform',
                    'network': 'network',
                },
                'location_map': {
                    'platform': 'path',
                    'network': 'path',
                    'signed_tx': 'body',
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
            api_client=api_client,
            callable=__tx_send
        )
