"""
    Ubiquity REST API

    Ubiquity provides a RESTful and uniform way to access blockchain resources, with a rich and reusable model across multiple cryptocurrencies.  [Documentation](https://app.blockdaemon.com/docs/ubiquity)  ### Protocols #### Mainnet The following protocols are currently supported: * bitcoin * ethereum * polkadot * xrp * algorand * stellar  #### Testnet Testnet support coming soon  ##### Pagination Certain resources contain a lot of data, more than what's practical to return for a single request. With the help of pagination, the data is split across multiple responses. Each response returns a subset of the items requested and a continuation token.  To get the next batch of items, copy the returned continuation token to the continuation query parameter and repeat the request with the new URL. In case no continuation token is returned, there is no more data available.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@blockdaemon.com
    Generated by: https://openapi-generator.tech
"""

import unittest

import test.mock
import test.utils
import ubiquity
from ubiquity.api import (
    sync_api,
    ApiClient,
)
from ubiquity import Configuration

import httpretty
import urllib3


class TestSyncApi(unittest.TestCase):
    """SyncApi unit test stubs"""
    def setUp(self):
        self.api_client = ApiClient(Configuration())
        self.api_instance = sync_api.SyncApi(self.api_client)  # noqa: E501
        self.platforms = test.utils.get_platforms()

    def tearDown(self):
        pass

    # Helper methods
    def get_sync_endpoints(self, network, path):
        endpoints = [{
            "req_url":
            f"/{platform}/{network}/sync/block_{path}",
            "method":
            httpretty.GET,
            "status":
            200,
            "response_data":
            test.mock.get_mock_file_content(f'sync_api/sync_block_{path}_{platform}.json')
        } for platform in self.platforms]
        return endpoints

    def call_endpoints(self, test_type, endpoints, platforms):
        for platform in self.platforms:
            try:
                if test_type == "number":
                    _ = self.api_instance.current_block_number(platform)
                if test_type == "id":
                    _ = self.api_instance.current_block_id(platform)
            except Exception as e:
                raise e



    # Tests
    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_sync_block_number(self):
        network = "mainnet"
        endpoints = self.get_sync_endpoints(network, "number")
        test.mock.setup_mock_server(self.api_client.configuration.host,
                                    endpoints)

        self.call_endpoints("number", endpoints, self.platforms)

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_sync_block_id(self):
        network = "mainnet"
        endpoints = self.get_sync_endpoints(network, "id")
        test.mock.setup_mock_server(self.api_client.configuration.host,
                                    endpoints)

        self.call_endpoints("id", endpoints, self.platforms)

if __name__ == '__main__':
    unittest.main()
