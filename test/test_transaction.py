import json
import unittest

import test.mock
import test.utils

import httpretty
import ubiquity.transaction as tx
from ubiquity import Configuration
from ubiquity.api import (
    transactions_api,
    ApiClient,
)

class TestTransactions(unittest.TestCase):
    def setUp(self):
        self.api_client = ApiClient(Configuration())

    def tearDown(self):
        pass

    def test_create_bitcoin_transaction_single_destination(self):
        from_ = [{
            "address": "6b4510d1dd716f49c6c701d8d0ad47af3d07847660dc4e1b25e10516714a7f31",
            "index": 0
        }]
        to = [
            {
                "address": "mmDDkcfXF5co6itzXrivWyxut7XifYywtR",
                "amount": 97990
            },
            {
                "address": "mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt",
                "amount": 10
            }
        ]
        fee = 1000

        network = "testnet"

        unsigned_tx = tx.create_bitcoin(from_, to, fee, { "network": network })

        unsigned_expected = "0100000001317f4a711605e1251b4edc607684073daf47add0d801c7c6496f71ddd110456b0000000000ffffffff02c67e0100000000001976a9143e762bc9a952a0aeb30c79491921151e7d412f6b88ac0a000000000000001976a914344a0f48ca150ec2b903817660b9b68b13a6702688ac00000000"
        assert unsigned_tx == unsigned_expected

    def test_sign_bitcoin_transaction_single_input_and_destination(self):
        signing_key = "92VNZDvn5NWbtALVxv6s1cKdKVq4Udd6zQ6SxgVK87qE3x7gZEZ"

        from_ = [{
            "address": "6b4510d1dd716f49c6c701d8d0ad47af3d07847660dc4e1b25e10516714a7f31",
            "index": 0
        }]
        to = [
            {
                "address": "mmDDkcfXF5co6itzXrivWyxut7XifYywtR",
                "amount": 97990
            },
            {
                "address": "mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt",
                "amount": 10
            }
        ]
        fee = 1000

        network = "testnet"

        signed_tx = tx.create_and_sign_bitcoin(from_, to, fee, signing_key, { "network": network })

        signed_expected = "0100000001317f4a711605e1251b4edc607684073daf47add0d801c7c6496f71ddd110456b000000008b483045022100ee8b153da42ee923050644bc154391a32d4e2ce6d05b69a32622d5b8f2ab520f02204e94f1b27574c8f72fca167cf5d6bb5bd324df71258539b839e07d586226fb9d014104a8db88ba9cc7ee9f5530e87a2a523d2fa9a4cfd1923c756c6590cdb7dd12745ee0a641a6b4314a5dbd251d7a8157dc8d0f20df2aa01b606f543902e523d5b9d1ffffffff02c67e0100000000001976a9143e762bc9a952a0aeb30c79491921151e7d412f6b88ac0a000000000000001976a914344a0f48ca150ec2b903817660b9b68b13a6702688ac00000000"
        assert signed_tx == signed_expected

    def test_sign_bitcoin_transaction_multiple_input(self):
        signing_key = "92VNZDvn5NWbtALVxv6s1cKdKVq4Udd6zQ6SxgVK87qE3x7gZEZ"

        from_ = [
            {
                "address": "ff2a60b53cd8bf4637dfd508a425d80b626da2ac929011094cf390b17327778a",
                "index": 0
            }, # newest, 0.0005 BTC
            {
                "address": "35b9e6de6d4141f6b23a9b707c2f60cba58a9ac4fba6d54b3ded336110183426",
                "index": 0
            } # oldest, 0.00096 BTC
        ]
        to = [
            {
                "address": "mmDDkcfXF5co6itzXrivWyxut7XifYywtR",
                "amount": 143000
            },
            {
                "address": "mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt",
                "amount": 1000
            },
            {
                "address": "tb1qj3kpr7fve8ht40lvvplc6rm8n7r9nxvj8zppuz",
                "amount": 1000
            }
        ]
        fee = 1000

        network = "testnet"

        signed_tx = tx.create_and_sign_bitcoin(from_, to, fee, signing_key, { "network": network })
        print(signed_tx)

        signed_expected = "01000000028a772773b190f34c09119092aca26d620bd825a408d5df3746bfd83cb5602aff000000008b483045022100b3d3fa315f0d3119de2ad80e48c1a95017f843e350e823971dcedcdefca38348022060d2e7d59c10205b16da378be61ee2f0ab365dbff6568f589c696b60d4b93890014104a8db88ba9cc7ee9f5530e87a2a523d2fa9a4cfd1923c756c6590cdb7dd12745ee0a641a6b4314a5dbd251d7a8157dc8d0f20df2aa01b606f543902e523d5b9d1ffffffff263418106133ed3d4bd5a6fbc49a8aa5cb602f7c709b3ab2f641416ddee6b935000000008a47304402200b60149d972e1a323154f534873666e9d7640d37ddb6c0847e83de9feee6c834022038ad6179401353d4a8eed4f89053be7d90167bb6335cfdbb49451d7dc02aa4ba014104a8db88ba9cc7ee9f5530e87a2a523d2fa9a4cfd1923c756c6590cdb7dd12745ee0a641a6b4314a5dbd251d7a8157dc8d0f20df2aa01b606f543902e523d5b9d1ffffffff03982e0200000000001976a9143e762bc9a952a0aeb30c79491921151e7d412f6b88ace8030000000000001976a914344a0f48ca150ec2b903817660b9b68b13a6702688ace803000000000000160014946c11f92cc9eebabfec607f8d0f679f8659999200000000"
        assert signed_tx == signed_expected

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_create_sign_ethereum_transaction_single_destination(self):
        platform = "ethereum"
        network = "ropsten"
        test.mock.setup_mock_server(
            self.api_client.configuration.host,
            [{
                "req_url":
                f"/{platform}/{network}/tx/estimate_fee",
                "method":
                httpretty.GET,
                "status":
                200,
                "response_data": "\"21000000000\"" }])

        signing_key = "1a96c5f08783afbd792d78212df8542fee62d79d33264626e225344de2c89742"

        from_ = [{
            "address": "0xb77aC006Bfe3C860441Fb3bD0726Fe57C0428aa9",
            "index": 3
        }]
        to = [{
                "address": "0x78c115F1c8B7D0804FbDF3CF7995B030c512ee78",
                "amount": 10 ** 18
        }]
        fee = 21000


        signed_tx = tx.create_and_sign_ethereum(from_, to, fee, signing_key, { "api_client": self.api_client, "network": network })

        signed_expected = "0xf864038504e3b292008252089478c115f1c8b7d0804fbdf3cf7995b030c512ee7801802aa08826c19d0979386b9849a55e9d3f5e72921ca1468a40478392bd2c6c10a3196ea06cf3b40361fe57abcd568cacab41ca38b3bf3df8fd5dce9ed31b2887977fe24a"
        assert signed_tx == signed_expected
    def test_create_sign_ethereum_transaction_multiple_destination_error(self):
        signing_key = "key"

        from_ = [{"address": "from", "index": 0}]
        to = [
            {
                "address": "dest1",
                "amount": 1
            },
            {
                "address": "dest2",
                "amount": 1
            }
        ]
        fee = 0

        network = "ropsten"

        try:
            tx.create_and_sign_ethereum(from_, to, fee, signing_key, { "api_client": self.api_client, "network": network })
        except tx.TxCreationError:
            return

        raise AssertionError("Expected a TxCreationError exception to be raised")

    def test_create_sign_ethereum_transaction_multiple_destination_error(self):
        signing_key = "key"

        from_ = [{
            "address": "from",
            "index": 0
        }]
        to = [
            {
                "address": "dest1",
                "amount": 1
            },
            {
                "address": "dest2",
                "amount": 1
            }
        ]
        fee = 0

        network = "ropsten"

        try:
            tx.create_and_sign_ethereum(from_, to, fee, signing_key, { "api_client": self.api_client, "network": network })
        except tx.TxCreationError:
            return

        raise AssertionError("Expected a TxCreationError exception to be raised")


if __name__ == '__main__':
    unittest.main()
