import argparse
import requests

parser = argparse.ArgumentParser()

url = parser.add_argument('--url',
                          action='store',
                          help='define url',
                          default='https://ya.ru',
                          required=False)

status_code = parser.add_argument('--status_code',
                                  action='store',
                                  help='define the status code',
                                  default='200',
                                  required=False)


def test_status_code_ok_for_breeds(url):
    r = requests.get(url)
    assert r.status_code == status_code

args = parser.parse_args()
print(args)
