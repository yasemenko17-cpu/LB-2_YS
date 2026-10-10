"""Автоматична перевірка варіанта 15."""
import pytest
from conftest import load
from kits import lab02

V = load(15)
CASES = [{'id': 'звичайний запит',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'video.lab.test',
  'path': '/watch',
  'expect': {'kind': 'proxy',
             'upstream': 'http://127.0.0.1:9015',
             'servers': ['127.0.0.1:9015'],
             'path': '/watch'}},
 {'id': 'генерація сертифіката',
  'public': True,
  'kind': 'tls',
  'args': [],
  'certs': [{'path': 'certs/video.crt',
             'expect': {'cn': '*.lab.test',
                        'sans': ['DNS:*.lab.test', 'DNS:lab.test'],
                        'days': 180,
                        'alg': 'id-ecPublicKey',
                        'curve': 'prime256v1',
                        'self_signed': True}}]}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_lab_15(case):
    lab02.check(V, case)
