"""Автоматична перевірка варіанта 10."""
import pytest
from conftest import load
from kits import lab02

V = load(10)
CASES = [{'id': 'блог: заборона',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'blog.lab.test',
  'path': '/admin/settings',
  'expect': {'kind': 'return', 'code': 403}},
 {'id': 'tls: rsa',
  'public': True,
  'kind': 'tls',
  'args': [],
  'certs': [{'path': 'certs/blog.crt',
             'expect': {'cn': 'blog.lab.test',
                        'days': 30,
                        'alg': 'rsaEncryption',
                        'bits': 3072,
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_10(case):
    lab02.check(V, case)
