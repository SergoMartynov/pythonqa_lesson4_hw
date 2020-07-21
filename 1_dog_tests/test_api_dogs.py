import json
import requests
from jsonschema import validate


def test_status_code_ok_for_breeds(base_url):
    r = requests.get(base_url + '/image/random')
    assert r.status_code == 200


def test_status_code_not_ok_for_breeds(base_url):
    r = requests.get(base_url + '/image/random1')
    assert r.status_code == 404


def test_jsonschema(base_url, schema):
    requests.get(base_url + '/image/random')
    validate({'status': 'success'}, schema=schema)


def test_subbreed(base_url, schema_subbreed):
    requests.get(base_url + '/hound/list')
    validate({'status': 'success', 'message': ['afghan']}, schema=schema_subbreed)


def test_number_of_image(base_url):
    r = requests.get(base_url + '/image/random/3')
    item_dict = json.loads(r.text)
    number_of_images = len(item_dict['message'])
    assert number_of_images == 3
