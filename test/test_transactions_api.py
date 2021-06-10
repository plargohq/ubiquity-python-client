"""
    Ubiquity REST API

    Ubiquity provides a RESTful and uniform way to access blockchain resources, with a rich and reusable model across multiple cryptocurrencies.  [Documentation](https://app.blockdaemon.com/docs/ubiquity)  ### Protocols #### Mainnet The following protocols are currently supported: * bitcoin * ethereum * polkadot * xrp * algorand * stellar  #### Testnet Testnet support coming soon  ##### Pagination Certain resources contain a lot of data, more than what's practical to return for a single request. With the help of pagination, the data is split across multiple responses. Each response returns a subset of the items requested and a continuation token.  To get the next batch of items, copy the returned continuation token to the continuation query parameter and repeat the request with the new URL. In case no continuation token is returned, there is no more data available.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@blockdaemon.com
    Generated by: https://openapi-generator.tech
"""

import json
import unittest

import test.mock
import test.utils
import ubiquity
from ubiquity.api import (
    transactions_api,
    ApiClient,
)
from ubiquity import Configuration

import httpretty
import urllib3


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""
    def setUp(self):
        self.api_client = ApiClient(Configuration())
        self.api_instance = transactions_api.TransactionsApi(
            self.api_client)  # noqa: E501
        self.platforms = test.utils.get_platform_enum_values()

    def tearDown(self):
        pass

    # Helper methods
    def get_supported_platforms(self, endpoint):
        return [
            p for p in self.platforms
            if test.mock.is_platform_supported(p, endpoint)
        ]

    def get_transactions_endpoints(self, network, path, supported_platforms,
                                   transactions_by_platform):
        endpoints_data_platforms = []
        parsed_transactions_platforms = []
        for platform in supported_platforms:
            parsed_transactions = json.loads(transactions_by_platform[platform])
            parsed_transactions_platforms.append(parsed_transactions)
            endpoints_data_platforms.append(
                {
                    "req_url":
                    f"/{platform}/{network}/{'tx/' + parsed_transactions['items'][0]['id'] if path == 'tx' else path}",
                    "method":
                    httpretty.GET,
                    "status":
                    200,
                    "response_data":
                    json.dumps(parsed_transactions['items'][0])
                    if path == "tx" else transactions_by_platform[platform]
                }
            )
        return endpoints_data_platforms, parsed_transactions_platforms

    def get_transactions_by_supported_platforms(self, supported_platforms):
        return {
            platform: test.mock.get_mock_file_content(
                f'transactions_api/get_txs_{platform}.json')
            for platform in supported_platforms
        }

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_get_txs(self):
        network = "mainnet"
        supported_platforms = test.mock.get_supported_platforms(self.platforms, "/txs")
        transactions_by_platform = self.get_transactions_by_supported_platforms(
            supported_platforms)
        endpoints, _ = self.get_transactions_endpoints(network, "txs",
                                                    supported_platforms,
                                                    transactions_by_platform)
        test.mock.setup_mock_server(self.api_client.configuration.host,
                                    endpoints)
        assert len(supported_platforms) > 1
        for platform in supported_platforms:
            try:
                _ = self.api_instance.get_txs(platform)
            except Exception as e:
                print('error when calling platform', platform)
                raise e

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_get_tx_by_id(self):
        network = "mainnet"
        supported_platforms = test.mock.get_supported_platforms(self.platforms, "/tx/:id")
        transactions_by_platform = self.get_transactions_by_supported_platforms(
            supported_platforms)
        endpoints, parsed_transactions = self.get_transactions_endpoints(network, "tx",
                                                    supported_platforms,
                                                    transactions_by_platform)
        test.mock.setup_mock_server(self.api_client.configuration.host,
                                    endpoints)
        assert len(supported_platforms) > 1
        for i, platform in enumerate(supported_platforms):
            print("calling tx_by_id for platform", platform)
            try:
                _ = self.api_instance.get_tx(
                    platform,
                    parsed_transactions[i]['items'][0]['id']
                )
            except Exception as e:
                print('error when calling platform', platform)
                raise e


if __name__ == '__main__':
    unittest.main()
