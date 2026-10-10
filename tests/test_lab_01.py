"""Автоматична перевірка варіанта 01."""
import pytest
from conftest import load
from kits import lab02

V = load(1)
CASES = [{'id': 'редирект на https',
  'public': True,
  'kind': 'nginx',
  'scheme': 'http',
  'host': 'shop.lab.test',
  'path': '/',
  'expect': {'kind': 'redirect', 'code': 301, 'location': 'https://shop.lab.test/'}},
 {'id': 'скрипт tls.sh',
  'public': True,
  'kind': 'tls',
  'args': ['shop.lab.test', '30'],
  'files': {},
  'stdout': '',
  'code': 0,
  'listing': {'.': ['shop.lab.test.crt', 'shop.lab.test.key']},
  'certs': [{'path': 'shop.lab.test.crt',
             'expect': {'cn': 'shop.lab.test',
                        'sans': ['DNS:shop.lab.test'],
                        'days': 30,
                        'alg': 'id-ecPublicKey',
                        'curve': 'P-256',
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_01(case):
    lab02.check(V, case)
