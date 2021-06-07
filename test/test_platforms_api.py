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
    platforms_api,
    ApiClient,
)
from ubiquity import Configuration

import httpretty
import urllib3


class TestPlatformsApi(unittest.TestCase):
    """PlatformsApi unit test stubs"""

    def setUp(self):
        self.api_client = ApiClient(Configuration())
        self.api_instance = platforms_api.PlatformsApi(self.api_client)  # noqa: E501
        self.platforms = test.utils.get_platform_enum_values()

        network = "mainnet"

        self.endpoints = [{
            "req_url": f"/{platform}/{network}",
            "method": httpretty.GET,
            "status": 200,
            "response_data": test.mock.get_mock_file_content(f'platform_{platform}.json')
        } for platform in self.platforms]


    def tearDown(self):
        pass

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_get_platform(self):
        test.mock.setup_mock_server(self.api_client.configuration.host, self.endpoints)

        for platform in self.platforms:
            try:
                _ = self.api_instance.get_platform(platform)
            except Exception as e:
                raise e


if __name__ == '__main__':
    unittest.main()
