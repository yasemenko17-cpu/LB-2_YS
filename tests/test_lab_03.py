"""Автоматична перевірка варіанта 03."""
import pytest
from conftest import load
from kits import lab02

V = load(3)
CASES = [{'id': 'проксі api',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'video.lab.test',
  'path': '/api/login',
  'expect': {'kind': 'proxy',
             'servers': ['127.0.0.1:9010'],
             'path': '/v1/login',
             'headers': {'Host': 'video.lab.test'}}},
 {'id': 'скрипт tls.sh',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'stdout': '',
  'code': 0,
  'listing': {'.': ['wildcard.crt', 'wildcard.key']},
  'certs': [{'path': 'wildcard.crt',
             'expect': {'cn': '*.lab.test',
                        'sans': ['DNS:*.lab.test', 'DNS:lab.test'],
                        'days': 180,
                        'alg': 'id-ecPublicKey',
                        'curve': 'P-256',
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_03(case):
    lab02.check(V, case)
