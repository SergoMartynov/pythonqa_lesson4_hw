import pytest
import requests
from jsonschema import validate


def test_status_code_ok_for_breeds():
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    assert r.status_code == 200

def test_status_code_not_ok_for_breeds():
    r = requests.get('https://dog.ceo/api/breeds/image/random1')
    assert r.status_code == 404


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
