"""Автоматична перевірка варіанта 18."""
import pytest
from conftest import load
from kits import lab02

V = load(18)
CASES = [{'id': 'маршрутизація api',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'maps.lab.test',
  'path': '/api/search',
  'expect': {'kind': 'proxy', 'servers': ['127.0.0.1:9018'], 'path': '/v1/search'}},
 {'id': 'сертифікат ECDSA',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'env': {},
  'stdout': '',
  'code': 0,
  'certs': [{'path': 'certs/maps.crt',
             'expect': {'cn': 'maps.lab.test',
                        'sans': ['DNS:api.maps.lab.test', 'DNS:maps.lab.test'],
                        'days': 90,
                        'alg': 'id-ecPublicKey',
                        'curve': 'prime256v1',
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_18(case):
    lab02.check(V, case)
