import requests
import pytest
from jsonschema import validate


def test_breweries_list(base_url):
    r = requests.get(base_url)
    assert r.status_code == 200

@pytest.mark.parametrize("city_test", ['san_diego', 'amsterdam', 'new_york'])
def test_filetr_by_city(base_url, city_test):
    response = requests.get(base_url + '?by_city={}'.format(city_test))
    assert response.status_code == 200

@pytest.mark.parametrize("city_test", ['san_diego', 'amsterdam', 'new_york'])
def test_filetr_by_city(base_url, city_test, schema):
    response = requests.get(base_url + '?by_city={}'.format(city_test))
    validate({'city': [city_test]}, schema=schema)