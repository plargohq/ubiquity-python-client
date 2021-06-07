import json
import os.path
import httpretty

MOCK_FILE_DIR = 'mock_files'

def get_mock_file_content(path):
    """
        Gets the content of file located under path
                relative to the test/mock_files directory
    """
    cur_dir = os.path.dirname(__file__)

    file = open(os.path.join(cur_dir, MOCK_FILE_DIR, path))
    return file.read()


def setup_mock_server(base_url, endpoints):
    """
        Setup httpretty mock server
    """
    for endpoint_data in endpoints:
        req_url = base_url + endpoint_data["req_url"]
        httpretty.register_uri(endpoint_data["method"],
                               req_url,
                               status=endpoint_data["status"],
                               body=endpoint_data["response_data"])
