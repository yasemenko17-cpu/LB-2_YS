"""Автоматична перевірка варіанта 30."""
import pytest
from conftest import load
from kits import lab02

V = load(30)
CASES = [{'id': 'проксі та заголовки',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'map.lab.test',
  'path': '/',
  'expect': {'kind': 'proxy',
             'servers': ['127.0.0.1:9030'],
             'headers': {'Host': 'map.lab.test', 'X-Real-IP': 'CLIENT', 'X-Forwarded-For': 'CLIENT'}}},
 {'id': 'генерація tls',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'code': 0,
  'certs': [{'path': 'map.crt',
             'expect': {'cn': 'map.lab.test',
                        'sans': ['DNS:map.lab.test', 'DNS:www.map.lab.test'],
                        'days': 90,
                        'alg': 'id-ecPublicKey',
                        'curve': 'P-256'}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_30(case):
    lab02.check(V, case)
