import pytest
import requests


def test_url_status_code(url, my_status_code):
    r = requests.get(url)
    print('\n url is:')
    print(url)
    print('\n my status_code is')
    print(my_status_code)
    print('\n responded status_code is')
    print(r.status_code)
    assert r.status_code == my_status_code
