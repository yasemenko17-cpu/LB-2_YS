"""Автоматична перевірка варіанта 28."""
import pytest
from conftest import load
from kits import lab02

V = load(28)
CASES = [{'id': 'головна сторінка',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'wiki.lab.test',
  'path': '/',
  'expect': {'kind': 'static', 'root': '/var/www/wiki28'}},
 {'id': 'генерація tls',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'code': 0,
  'certs': [{'path': 'wiki.crt',
             'expect': {'cn': 'wiki.lab.test',
                        'sans': ['DNS:wiki.lab.test'],
                        'days': 30,
                        'alg': 'rsaEncryption',
                        'bits': 3072}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_28(case):
    lab02.check(V, case)
