import pytest
import requests


class APIClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, path='/', params=None):
        url = self.base_address + path
        print('Get request to {}'.format(url))
        return requests.get(url=url, params=params)


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        action='store',
        default='https://jsonplaceholder.typicode.com',
        help='This is requested URL'
    )


@pytest.fixture(scope='session')
def api_client(request):
    base_url = request.config.getoption('--url')
    return APIClient(base_address=base_url)
