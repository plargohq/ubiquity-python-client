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

    def test_create_bitcoin_transaction_single_input(self):
        from_ = [{
            "address":
            "6b4510d1dd716f49c6c701d8d0ad47af3d07847660dc4e1b25e10516714a7f31",
            "index": 0
        }]

        to = [{
            "address": "mmDDkcfXF5co6itzXrivWyxut7XifYywtR",
            "amount": 97990
        }, {
            "address": "mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt",
            "amount": 10
        }]

        network = "testnet"

        unsigned_tx = tx.create_bitcoin(from_, to, {"network": network})

        unsigned_expected = "0100000001317f4a711605e1251b4edc607684073daf47add0d801c7c6496f71ddd110456b0000000000ffffffff02c67e0100000000001976a9143e762bc9a952a0aeb30c79491921151e7d412f6b88ac0a000000000000001976a914344a0f48ca150ec2b903817660b9b68b13a6702688ac00000000"
        assert unsigned_tx == unsigned_expected

    def test_sign_bitcoin_transaction_single_input_and_destination(self):
        signing_key = "92VNZDvn5NWbtALVxv6s1cKdKVq4Udd6zQ6SxgVK87qE3x7gZEZ"

        from_ = [{
            "address":
            "6b4510d1dd716f49c6c701d8d0ad47af3d07847660dc4e1b25e10516714a7f31",
            "index": 0
        }]
        to = [{
            "address": "mmDDkcfXF5co6itzXrivWyxut7XifYywtR",
            "amount": 97990
        }, {
            "address": "mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt",
            "amount": 10
        }]

        network = "testnet"

        signed_tx = tx.create_and_sign_bitcoin(from_, to, signing_key,
                                               {"network": network})

        signed_expected = "0100000001317f4a711605e1251b4edc607684073daf47add0d801c7c6496f71ddd110456b000000008b483045022100cd79f27cdf5c6bbd9284c07308adee9d814ce06c8801ee8df1e26929f71b3682022008a70f9283913e0c7b121f837f33ffe9882c3e83c9ec4ea6912d275ffbf713ab014104a8db88ba9cc7ee9f5530e87a2a523d2fa9a4cfd1923c756c6590cdb7dd12745ee0a641a6b4314a5dbd251d7a8157dc8d0f20df2aa01b606f543902e523d5b9d1ffffffff02c67e0100000000001976a9143e762bc9a952a0aeb30c79491921151e7d412f6b88ac0a000000000000001976a914344a0f48ca150ec2b903817660b9b68b13a6702688ac00000000"
        assert signed_tx == signed_expected

    def test_sign_bitcoin_transaction_multiple_input(self):
        signing_key = "92VNZDvn5NWbtALVxv6s1cKdKVq4Udd6zQ6SxgVK87qE3x7gZEZ"

        from_ = [{
            "address":
            "a287e3d84fca57bc06d7d0b04e8fcf0bae2226dd27f077709b40e7168eba89d9",
            "index": 0
        }, {
            "address":
            "6c8c9213b2e10f2fef032d08c6dddf24bbb85109437abbe434e8ae53bde2e859",
            "index": 0
        }]

        to = [{
            "address": "mmDDkcfXF5co6itzXrivWyxut7XifYywtR",
            "amount": 119000
        }, {
            "address": "mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt",
            "amount": 1000
        }]

        network = "testnet"

        signed_tx = tx.create_and_sign_bitcoin(from_, to, signing_key,
                                               {"network": network})

        signed_expected = "0100000002d989ba8e16e7409b7077f027dd2622ae0bcf8f4eb0d0d706bc57ca4fd8e387a2000000008b483045022100ade5005f6b771f9579eaa5e148f47e551b834947b54209fbbf316bc23a88302602202c3e03038ffb43d2d575f351145aa2d1fcc27b879bb2ba2ddc9d4577c5037ed8014104a8db88ba9cc7ee9f5530e87a2a523d2fa9a4cfd1923c756c6590cdb7dd12745ee0a641a6b4314a5dbd251d7a8157dc8d0f20df2aa01b606f543902e523d5b9d1ffffffff59e8e2bd53aee834e4bb7a430951b8bb24dfddc6082d03ef2f0fe1b213928c6c000000008b483045022100dbafb0109a65718dc57d3d4d4f682adee12a4b3a2c8581439e8829dba0b33061022019016f0b6e2ffe3e65458e42fb736998d45da20f13983a9bf9784a20bc3b87ea014104a8db88ba9cc7ee9f5530e87a2a523d2fa9a4cfd1923c756c6590cdb7dd12745ee0a641a6b4314a5dbd251d7a8157dc8d0f20df2aa01b606f543902e523d5b9d1ffffffff02d8d00100000000001976a9143e762bc9a952a0aeb30c79491921151e7d412f6b88ace8030000000000001976a914344a0f48ca150ec2b903817660b9b68b13a6702688ac00000000"
        assert signed_tx == signed_expected

    @httpretty.activate(verbose=True, allow_net_connect=False)
    def test_create_sign_ethereum_transaction_single_destination(self):
        platform = "ethereum"
        network = "ropsten"
        test.mock.setup_mock_server(
            self.api_client.configuration.host,
            [{
                "req_url": f"/{platform}/{network}/tx/estimate_fee",
                "method": httpretty.GET,
                "status": 200,
                "response_data": "\"21000000000\""
            }])

        signing_key = "1a96c5f08783afbd792d78212df8542fee62d79d33264626e225344de2c89742"

        from_ = [{
            "address": "0xb77aC006Bfe3C860441Fb3bD0726Fe57C0428aa9",
            "index": 3
        }]
        to = [{
            "address": "0x78c115F1c8B7D0804FbDF3CF7995B030c512ee78",
            "amount": 1
        }]

        fee = 21000

        signed_tx = tx.create_and_sign_ethereum(from_, to, signing_key, {
            "api_client": self.api_client,
            "network": network,
            "fee": fee
        })

        signed_expected = "0xf864038504e3b292008252089478c115f1c8b7d0804fbdf3cf7995b030c512ee7801802aa08826c19d0979386b9849a55e9d3f5e72921ca1468a40478392bd2c6c10a3196ea06cf3b40361fe57abcd568cacab41ca38b3bf3df8fd5dce9ed31b2887977fe24a"
        assert signed_tx == signed_expected

    def test_create_sign_ethereum_transaction_multiple_destination_error(self):
        signing_key = "key"

        from_ = [{"address": "from", "index": 0}]
        to = [{
            "address": "dest1",
            "amount": 1
        }, {
            "address": "dest2",
            "amount": 1
        }]

        network = "ropsten"

        try:
            tx.create_and_sign_ethereum(from_, to, signing_key, {
                "api_client": self.api_client,
                "network": network,
                "fee": 0
            })
        except tx.TxCreationError:
            return

        raise AssertionError(
            "Expected a TxCreationError exception to be raised")


if __name__ == '__main__':
    unittest.main()
