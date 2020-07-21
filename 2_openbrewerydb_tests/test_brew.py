import requests
import pytest
from jsonschema import validate


def test_breweries_list(base_url):
    r = requests.get(base_url)
    assert r.status_code == 200


def test_404(base_url):
    r = requests.get(base_url + '/0')
    assert r.status_code == 404


def test_validation_id0(base_url, schema_id0):
    r = response = requests.get(base_url + '/0')
    validate({'message': "Couldn't find Brewery with 'id'=0"}, schema=schema_id0)


def test_validation_id1(base_url, schema_id1):
    r = requests.get(base_url + '/1')
    validate({'id': 1}, schema=schema_id1)


@pytest.mark.parametrize("city_test", ['san_diego', 'amsterdam', 'new_york'])
def test_filetr_by_city(base_url, city_test):
    response = requests.get(base_url + '?by_city={}'.format(city_test))
    assert response.status_code == 200
