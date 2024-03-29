import json
import os.path
import httpretty

MOCK_FILE_DIR = 'mock_files'


def get_mock_file_content(path):
    """
        Gets the content of file located under path
                relative to the test/mock_files directory
    """
    cur_dir = os.path.abspath(os.path.dirname(__file__))

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


def is_platform_supported(platform, endpoint):
    """
        Gets mock about platform information and returns True
        if the endpoint is supported by it according to the info
    """
    platform_data_mock_file = get_mock_file_content(
        f"platforms_api/platform_{platform}.json")
    platform_json_mock_data = json.loads(platform_data_mock_file)
    return endpoint in platform_json_mock_data["endpoints"]


def get_supported_platforms(platforms, endpoint):
    """
        Gets platforms that support 'endpoint' according to mocked
            response obtained by 'is_platform_supported'
    """
    return [
        p for p in platforms if is_platform_supported(p, endpoint)
    ]
