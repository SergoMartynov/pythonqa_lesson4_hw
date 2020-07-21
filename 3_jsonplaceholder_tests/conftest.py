import pytest

@pytest.fixture
def base_url():
    url = 'https://jsonplaceholder.typicode.com/posts'
    return url


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


@pytest.fixture()
def schema_id101():
    schema = {
        'type': 'object',
        'properties': {
            'id': {'type': 'integer',
                       'enum': [101]}
            },
    }
    return schema