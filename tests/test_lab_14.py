"""Автоматична перевірка варіанта 14."""
import pytest
from conftest import load
from kits import lab02

V = load(14)
CASES = [{'id': 'редирект http',
  'public': True,
  'kind': 'nginx',
  'scheme': 'http',
  'host': 'tasks.lab.test',
  'path': '/issue/5',
  'expect': {'kind': 'redirect', 'code': 301, 'location': 'https://tasks.lab.test/issue/5'}},
 {'id': 'приховані метрики',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'tasks.lab.test',
  'path': '/metrics',
  'expect': {'kind': 'return', 'code': 404}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_14(case):
    lab02.check(V, case)
