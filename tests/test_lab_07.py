"""Автоматична перевірка варіанта 07."""
import pytest
from conftest import load
from kits import lab02

V = load(7)
CASES = [{'id': 'платформа: wildcard',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'stream.lab.test',
  'path': '/play',
  'expect': {'kind': 'proxy', 'servers': ['127.0.0.1:9020']}},
 {'id': 'tls: аргументи',
  'public': True,
  'kind': 'tls',
  'args': ['auth.lab.test', '60'],
  'certs': [{'path': 'certs/video.crt',
             'expect': {'cn': 'auth.lab.test',
                        'sans': ['DNS:*.lab.test', 'DNS:auth.lab.test'],
                        'days': 60,
                        'alg': 'id-ecPublicKey',
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_07(case):
    lab02.check(V, case)
