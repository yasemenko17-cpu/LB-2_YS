"""Автоматична перевірка варіанта 24."""
import pytest
from conftest import load
from kits import lab02

V = load(24)
CASES = [{'id': 'проксі websocket',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'tasks.lab.test',
  'path': '/ws/board',
  'expect': {'kind': 'proxy',
             'upstream': 'tasks_backend',
             'path': '/ws/board',
             'headers': {'Connection': 'upgrade'}}},
 {'id': 'статика корінь',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'tasks.lab.test',
  'path': '/',
  'expect': {'kind': 'static', 'root': '/var/www/tasks'}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_24(case):
    lab02.check(V, case)
