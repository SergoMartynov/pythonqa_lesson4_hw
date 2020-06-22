import pytest
import requests
from jsonschema import validate


@pytest.fixture
def base_url():
    url = 'https://dog.ceo/api/breeds'
    return url


def test_status_code_ok_for_breeds(base_url):
    r = requests.get(base_url + '/image/random')
    assert r.status_code == 200


def test_status_code_not_ok_for_breeds(base_url):
    r = requests.get(base_url + '/image/random1')
    assert r.status_code == 404


def test_jsonschema(base_url):
    r = requests.get(base_url + '/image/random')
    schema = {
        'type': 'object',
        'properties': {
            'message': {'type': 'string'},
            'status': {'type': 'string'}
        },
    }
    validate({'status': 'success'}, schema=schema)







# def test_images_for_breeds()


# schema = {
#     'type': 'object',
#     'properties': {
#         'message': {'type': 'string'},
#         'status': {'type': 'string'}
#     },
#     'required': ['message', 'status']
# }
#
# validate(instance=res.json(), schema=schema)

{
    "message": "https://images.dog.ceo/breeds/malinois/n02105162_4719.jpg",
    "status": "success"
}
