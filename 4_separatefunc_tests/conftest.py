import pytest


def pytest_addoption(parser):
    parser.addoption('--url',
                     help='define url',
                     default='https://ya.ru/',
                     required=False)

    parser.addoption('--status_code',
                     type='int',
                     help='define the status code',
                     default=200,
                     choices=[200, 404],
                     required=False)


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def my_status_code(request):
    return request.config.getoption('--status_code')
