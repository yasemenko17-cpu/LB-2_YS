"""Автоматична перевірка варіанта 08."""
import pytest
from conftest import load
from kits import lab02

V = load(8)
CASES = [{'id': 'health точний',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'tasks.lab.test',
  'path': '/health',
  'expect': {'kind': 'return', 'code': 200, 'body': 'OK'}},
 {'id': 'tls: створення',
  'public': True,
  'kind': 'tls',
  'args': [],
  'certs': [{'path': 'certs/tasks.crt',
             'expect': {'cn': 'tasks.lab.test', 'alg': 'id-ecPublicKey', 'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_08(case):
    lab02.check(V, case)
