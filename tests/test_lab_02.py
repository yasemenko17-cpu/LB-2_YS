"""Автоматична перевірка варіанта 02."""
import pytest
from conftest import load
from kits import lab02

V = load(2)
CASES = [{'id': 'балансування запитів',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'wiki.lab.test',
  'path': '/',
  'expect': {'kind': 'proxy',
             'upstream': 'wiki_backend',
             'path': '/',
             'headers': {'Host': 'wiki.lab.test', 'X-Forwarded-Proto': 'https'}}},
 {'id': 'скрипт tls.sh',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'stdout': '',
  'code': 0,
  'listing': {'certs': ['wiki.crt', 'wiki.key']},
  'certs': [{'path': 'certs/wiki.crt',
             'expect': {'cn': 'wiki.lab.test',
                        'sans': ['DNS:wiki.lab.test'],
                        'days': 365,
                        'alg': 'id-ecPublicKey',
                        'curve': 'P-256',
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_02(case):
    lab02.check(V, case)
