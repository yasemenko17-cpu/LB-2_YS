"""Автоматична перевірка варіанта 29."""
import pytest
from conftest import load
from kits import lab02

V = load(29)
CASES = [{'id': 'редирект',
  'public': True,
  'kind': 'nginx',
  'scheme': 'http',
  'port': 80,
  'host': 'tasks.lab.test',
  'path': '/issue/1',
  'expect': {'kind': 'redirect', 'code': 301, 'location': 'https://tasks.lab.test/issue/1'}},
 {'id': 'генерація tls',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'code': 0,
  'certs': [{'path': 'tasks.crt',
             'expect': {'cn': 'tasks.lab.test',
                        'sans': ['DNS:tasks.lab.test', 'IP:127.0.0.1'],
                        'days': 365,
                        'alg': 'rsaEncryption',
                        'bits': 2048}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_29(case):
    lab02.check(V, case)
