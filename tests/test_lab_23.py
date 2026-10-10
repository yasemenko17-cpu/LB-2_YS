"""Автоматична перевірка варіанта 23."""
import pytest
from conftest import load
from kits import lab02

V = load(23)
CASES = [{'id': 'точний збіг health',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'blog.lab.test',
  'path': '/health',
  'expect': {'kind': 'return', 'code': 200, 'body': 'OK'}},
 {'id': 'regex для зображень',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'blog.lab.test',
  'path': '/photo.JPG',
  'expect': {'kind': 'static', 'root': '/var/www/images'}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_23(case):
    lab02.check(V, case)
