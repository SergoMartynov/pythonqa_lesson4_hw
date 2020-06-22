import pytest


@pytest.fixture
def base_url():
    url = 'https://dog.ceo/api/breeds'
    return url


@pytest.fixture()
def schema():
    schema = {
        'type': 'object',
        'properties': {
            'message': {'type': 'string'},
            'status': {'type': 'string',
                       'enum': ['success']}
        },
    }
    return schema


@pytest.fixture()
def schema_subbreed():
    schema = {
        'type': 'object',
        'properties': {
            'message': {'type': 'array', 'items': {'type': 'string',
                                                   'enum': [
                                                       "afghan",
                                                       "basset",
                                                       "blood",
                                                       "english",
                                                       "ibizan",
                                                       "plott",
                                                       "walker"]}},
            'status': {'type': 'string',
                       'enum': ['success']}
        },
    }
    return schema
