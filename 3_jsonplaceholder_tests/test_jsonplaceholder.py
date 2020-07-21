import pytest
import requests
from jsonschema import validate


def test_response_200(base_url):
    r = requests.get(base_url)
    assert r.status_code == 200

def test_response_404(base_url):
    r = requests.get(base_url + '/123')
    assert r.status_code == 404

def test_validation_id1(base_url, schema_id1):
    r = requests.get(base_url + '/1')
    validate({'id': 1}, schema=schema_id1)

def test_response_201(base_url):
    r = requests.post(base_url)
    assert r.status_code == 201

def test_validation_id101(base_url, schema_id101):
    r = requests.post(base_url)
    validate({'id': 101}, schema=schema_id101)

