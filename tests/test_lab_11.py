"""Автоматична перевірка варіанта 11."""
import pytest
from conftest import load
from kits import lab02

V = load(11)
CASES = [{'id': 'запит до api',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'shop.lab.test',
  'path': '/api/products',
  'expect': {'kind': 'proxy',
             'upstream': 'http://127.0.0.1:9011',
             'servers': ['127.0.0.1:9011'],
             'path': '/api/products'}},
 {'id': 'запит до статики',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'shop.lab.test',
  'path': '/index.html',
  'expect': {'kind': 'static', 'root': '/var/www/shop'}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_11(case):
    lab02.check(V, case)
