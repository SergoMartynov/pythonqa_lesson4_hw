import pytest
import requests
import argparse

def pytest_addoption(parser):
    parser.addoption






def test_status_code_ok_for_breeds(url):
    r = requests.get(url)
    assert r.status_code == status_code