import pytest


@pytest.fixture
def base_url():
    url = 'https://api.openbrewerydb.org/breweries'
    return url

@pytest.fixture()
def schema_id0():
    schema = {
        'type': 'object',
        'properties': {
            'message': {'type': 'string',
                       'enum': ["Couldn't find Brewery with 'id'=0"]}
            },
    }
    return schema


@pytest.fixture()
def schema_id1():
    schema = {
        'type': 'object',
        'properties': {
            'id': {'type': 'integer',
                       'enum': [1]}
            },
    }
    return schema


@pytest.fixture
def schema():
    schema = {
        'type': 'object',
        'properties': {
            "id": {'type': 'integer'},
            "name": {'type': 'string'},
            "brewery_type": {'type': 'string'},
            "street": {'type': 'string'},
            "city": {'type': 'string',
                     'enum': ['san_diego',
                              'amsterdam',
                              'new_york']},
            "state": {'type': 'string'},
            "postal_code": {'type': 'string'},
            "country": {'type': 'string'},
            "longitude": {'type': null},
            "latitude": {'type': null},
            "phone": {'type': 'string'},
            "website_url": {'type': 'string'},
            "updated_at": {'type': 'string'},
            "tag_list": []
        },
    }
    return schema

