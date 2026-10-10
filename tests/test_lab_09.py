"""Автоматична перевірка варіанта 09."""
import pytest
from conftest import load
from kits import lab02

V = load(9)
CASES = [{'id': 'карти: websocket',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'maps.lab.test',
  'path': '/ws/live',
  'expect': {'kind': 'proxy',
             'servers': ['127.0.0.1:9040'],
             'headers': {'Upgrade': '$http_upgrade', 'Connection': 'Upgrade'}}},
 {'id': 'tls: 180 днів',
  'public': True,
  'kind': 'tls',
  'args': [],
  'certs': [{'path': 'certs/maps.crt',
             'expect': {'cn': 'maps.lab.test',
                        'sans': ['DNS:*.lab.test', 'DNS:lab.test'],
                        'days': 180,
                        'alg': 'id-ecPublicKey',
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_09(case):
    lab02.check(V, case)
