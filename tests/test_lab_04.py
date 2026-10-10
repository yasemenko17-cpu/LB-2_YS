"""Автоматична перевірка варіанта 04."""
import pytest
from conftest import load
from kits import lab02

V = load(4)
CASES = [{'id': 'статика assets',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'tasks.lab.test',
  'path': '/assets/style.css',
  'expect': {'kind': 'static', 'root': '/var/www/tasks'}},
 {'id': 'скрипт tls.sh',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'stdout': '',
  'code': 0,
  'listing': {'.': ['tasks.crt', 'tasks.key']},
  'certs': [{'path': 'tasks.crt',
             'expect': {'cn': 'tasks.lab.test',
                        'sans': ['DNS:tasks.lab.test'],
                        'days': 30,
                        'alg': 'rsaEncryption',
                        'bits': 3072,
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_04(case):
    lab02.check(V, case)
