import ubiquity
from ubiquity.ubiquity_openapi_client import ApiClient as ApiClient_
from ubiquity.ubiquity_openapi_client.api import (
    accounts_api,
    blocks_api,
    platforms_api,
    sync_api,
    transactions_api,
)


class ApiClient(ApiClient_):
    def __init__(self, configuration):
        super(ApiClient, self).__init__(configuration)
