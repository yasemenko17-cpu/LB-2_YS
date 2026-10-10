"""Автоматична перевірка варіанта 17."""
import pytest
from conftest import load
from kits import lab02

V = load(17)
CASES = [{'id': 'проксі на бекенди',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'store.lab.test',
  'path': '/',
  'expect': {'kind': 'proxy', 'servers': ['127.0.0.1:9017', '127.0.0.1:9018'], 'path': '/'}},
 {'id': 'сертифікат із SAN',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'env': {},
  'stdout': '',
  'code': 0,
  'certs': [{'path': 'certs/store.crt',
             'expect': {'cn': 'store.lab.test',
                        'sans': ['DNS:store.lab.test', 'IP:127.0.0.1'],
                        'days': 365,
                        'alg': 'rsaEncryption',
                        'bits': 2048,
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_17(case):
    lab02.check(V, case)
