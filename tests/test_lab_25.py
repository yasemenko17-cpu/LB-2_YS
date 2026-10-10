"""Автоматична перевірка варіанта 25."""
import pytest
from conftest import load
from kits import lab02

V = load(25)
CASES = [{'id': 'заборона admin',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'maps.lab.test',
  'path': '/admin/users',
  'expect': {'kind': 'return', 'code': 403}},
 {'id': 'проксі tiles',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'maps.lab.test',
  'path': '/tiles',
  'expect': {'kind': 'proxy',
             'upstream': 'maps_backend',
             'path': '/tiles',
             'headers': {'X-Forwarded-Host': 'maps.lab.test'}}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_25(case):
    lab02.check(V, case)
