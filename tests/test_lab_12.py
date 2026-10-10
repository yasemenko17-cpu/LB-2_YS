"""Автоматична перевірка варіанта 12."""
import pytest
from conftest import load
from kits import lab02

V = load(12)
CASES = [{'id': 'звичайний запит',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'blog.lab.test',
  'path': '/post/1',
  'expect': {'kind': 'proxy',
             'upstream': 'http://127.0.0.1:9012',
             'servers': ['127.0.0.1:9012'],
             'path': '/post/1'}},
 {'id': 'запит сторінки помилки',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'blog.lab.test',
  'path': '/502.html',
  'expect': {'kind': 'static', 'root': '/var/www/blog'}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_12(case):
    lab02.check(V, case)
