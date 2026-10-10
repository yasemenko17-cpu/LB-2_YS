"""Автоматична перевірка варіанта 21."""
import pytest
from conftest import load
from kits import lab02

V = load(21)
CASES = [{'id': 'http редирект video',
  'public': True,
  'kind': 'nginx',
  'scheme': 'http',
  'host': 'video.lab.test',
  'path': '/watch',
  'expect': {'kind': 'redirect', 'code': 301, 'location': 'https://video.lab.test/watch'}},
 {'id': 'api проксі',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'api.lab.test',
  'path': '/users',
  'expect': {'kind': 'proxy',
             'upstream': 'api_backend',
             'path': '/users',
             'headers': {'Host': 'api.lab.test'}}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_21(case):
    lab02.check(V, case)
