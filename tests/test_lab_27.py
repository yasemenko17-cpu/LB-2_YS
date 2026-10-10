"""Автоматична перевірка варіанта 27."""
import pytest
from conftest import load
from kits import lab02

V = load(27)
CASES = [{'id': 'домашня сторінка',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'techblog.lab.test',
  'path': '/',
  'expect': {'kind': 'proxy',
             'servers': ['127.0.0.1:9027'],
             'path': '/',
             'headers': {'Host': 'techblog.lab.test'}}},
 {'id': 'генерація tls',
  'public': True,
  'kind': 'tls',
  'args': [],
  'files': {},
  'code': 0,
  'certs': [{'path': 'server.crt',
             'expect': {'cn': '*.lab.test',
                        'sans': ['DNS:*.lab.test', 'DNS:lab.test'],
                        'days': 180,
                        'alg': 'id-ecPublicKey',
                        'curve': 'P-256'}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_27(case):
    lab02.check(V, case)
