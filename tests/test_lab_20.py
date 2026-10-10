"""Автоматична перевірка варіанта 20."""
import pytest
from conftest import load
from kits import lab02

V = load(20)
CASES = [{'id': 'редирект з www',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'www.tasks.lab.test',
  'path': '/issue/1',
  'expect': {'kind': 'redirect', 'code': 301, 'location': 'https://tasks.lab.test/issue/1'}},
 {'id': 'генерація ECDSA',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'env': {},
  'stdout': '',
  'code': 0,
  'certs': [{'path': 'certs/tasks.crt',
             'expect': {'cn': 'tasks.lab.test',
                        'days': 365,
                        'alg': 'id-ecPublicKey',
                        'curve': 'prime256v1',
                        'self_signed': True,
                        'sans': ['DNS:tasks.lab.test', 'DNS:www.tasks.lab.test']}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_20(case):
    lab02.check(V, case)
