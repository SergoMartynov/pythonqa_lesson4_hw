import pytest
import requests


# @pytest.mark.parametrize("code", [200, 300, 400, 500])
# def test_url_status(url, code, method):
#     response = method(url + "/status/{}".format(code))
#     assert response.status_code == code


# def test_url_status(url, code, method):
#     response = method(url + "/status/{}".format(code))
#     assert response.status_code == code

def test_status_code(url, code):
    response = requests.get(url)
    assert response.status_code == code

