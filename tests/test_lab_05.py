"""Автоматична перевірка варіанта 05."""
import pytest
from conftest import load
from kits import lab02

V = load(5)
CASES = [{'id': 'редирект www',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'www.blog.lab.test',
  'path': '/about',
  'expect': {'kind': 'redirect', 'code': 301, 'location': 'https://blog.lab.test/about'}},
 {'id': 'скрипт tls.sh',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'stdout': '',
  'code': 0,
  'listing': {'.': ['blog.crt', 'blog.key']},
  'certs': [{'path': 'blog.crt',
             'expect': {'cn': 'blog.lab.test',
                        'sans': ['DNS:blog.lab.test', 'IP:127.0.0.1'],
                        'days': 365,
                        'alg': 'rsaEncryption',
                        'bits': 2048,
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_05(case):
    lab02.check(V, case)
