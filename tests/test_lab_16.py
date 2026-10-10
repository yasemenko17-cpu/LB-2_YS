"""Автоматична перевірка варіанта 16."""
import pytest
from conftest import load
from kits import lab02

V = load(16)
CASES = [{'id': 'редирект HTTP на HTTPS',
  'public': True,
  'kind': 'nginx',
  'scheme': 'http',
  'host': 'wiki.lab.test',
  'path': '/',
  'expect': {'kind': 'redirect', 'code': 301, 'location': 'https://wiki.lab.test/'}},
 {'id': 'генерує сертифікат RSA',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'env': {},
  'stdout': '',
  'code': 0,
  'certs': [{'path': 'certs/wiki.crt',
             'expect': {'cn': 'wiki.lab.test',
                        'days': 30,
                        'alg': 'rsaEncryption',
                        'bits': 3072,
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_16(case):
    lab02.check(V, case)
