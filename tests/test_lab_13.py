"""Автоматична перевірка варіанта 13."""
import pytest
from conftest import load
from kits import lab02

V = load(13)
CASES = [{'id': 'запит до адмінки з php',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'wiki.lab.test',
  'path': '/admin/index.php',
  'expect': {'kind': 'static', 'root': '/var/www/wiki'}},
 {'id': 'генерація з параметрами',
  'public': True,
  'kind': 'tls',
  'args': ['mywiki.test', '60'],
  'certs': [{'path': 'certs/wiki.crt',
             'expect': {'cn': 'mywiki.test',
                        'sans': ['DNS:mywiki.test'],
                        'days': 60,
                        'alg': 'id-ecPublicKey',
                        'curve': 'prime256v1',
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_13(case):
    lab02.check(V, case)
