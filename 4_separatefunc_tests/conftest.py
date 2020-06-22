import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru/",
        choices=["https://ya.ru/", "https://ya.ru/123"],
        help="This is requested url"
    )

    parser.addoption(
        "--status_code",
        default="200",
        choices=["200", "404"],
        help="Response status code"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def code(request):
    m = request.config.getoption("--status_code")
    if m == '200':
        return requests.status_codes
    elif m == '404':
        return requests.status_codes
