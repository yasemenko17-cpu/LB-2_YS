"""Автоматична перевірка варіанта 22."""
import pytest
from conftest import load
from kits import lab02

V = load(22)
CASES = [{'id': 'default_server невідомий',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'unknown.test',
  'path': '/',
  'expect': {'kind': 'return', 'code': 444}},
 {'id': 'проксі api',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'shop.lab.test',
  'path': '/api/books',
  'expect': {'kind': 'proxy', 'upstream': 'shop_backend', 'path': '/api/books'}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_22(case):
    lab02.check(V, case)
