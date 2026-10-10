"""Автоматична перевірка варіанта 26."""
import pytest
from conftest import load
from kits import lab02

V = load(26)
CASES = [{'id': 'запит до кореня',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'store.lab.test',
  'path': '/',
  'expect': {'kind': 'proxy', 'servers': ['127.0.0.1:9026'], 'headers': {'Host': 'store.lab.test'}}},
 {'id': 'створення ключів',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'code': 0,
  'certs': [{'path': 'certs/store.crt',
             'expect': {'cn': 'store.lab.test',
                        'alg': 'id-ecPublicKey',
                        'curve': 'P-256',
                        'days': 90,
                        'sans': ['DNS:store.lab.test']}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_26(case):
    lab02.check(V, case)
