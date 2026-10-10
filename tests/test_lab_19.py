"""Автоматична перевірка варіанта 19."""
import pytest
from conftest import load
from kits import lab02

V = load(19)
CASES = [{'id': 'статика assets',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'video.lab.test',
  'path': '/assets/logo.png',
  'expect': {'kind': 'static', 'root': '/var/www/video'}},
 {'id': 'сертифікат з аргументів',
  'public': True,
  'kind': 'tls',
  'args': ['video.lab.test', '45'],
  'files': {},
  'env': {},
  'stdout': '',
  'code': 0,
  'certs': [{'path': 'certs/video.crt',
             'expect': {'cn': 'video.lab.test',
                        'sans': ['DNS:video.lab.test'],
                        'days': 45,
                        'alg': 'id-ecPublicKey',
                        'curve': 'prime256v1',
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_19(case):
    lab02.check(V, case)
