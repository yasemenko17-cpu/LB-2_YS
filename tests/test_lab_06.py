"""Автоматична перевірка варіанта 06."""
import pytest
from conftest import load
from kits import lab02

V = load(6)
CASES = [{'id': 'вітрина: проксі',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'shop.lab.test',
  'path': '/',
  'expect': {'kind': 'proxy', 'servers': ['127.0.0.1:9010']}},
 {'id': 'tls: створення сертифіката',
  'public': True,
  'kind': 'tls',
  'args': [],
  'certs': [{'path': 'certs/shop.crt',
             'expect': {'cn': 'shop.lab.test',
                        'sans': ['DNS:api.shop.lab.test', 'DNS:shop.lab.test'],
                        'days': 90,
                        'alg': 'id-ecPublicKey',
                        'curve': 'P-256',
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_06(case):
    lab02.check(V, case)
