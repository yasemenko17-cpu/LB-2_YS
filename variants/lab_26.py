"""Службовий файл варіанта 26. Не змінюйте його: ви редагуєте файли в папці lab_26/."""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "lab_26"
FILES = ['nginx.conf', 'tls.sh']
for _name in FILES:
    if "TODO: реалізуйте" in (DIR / _name).read_text(encoding="utf-8"):
        raise NotImplementedError(f"Файл {_name} (варіанта 26) ще не реалізовано: виконайте завдання за карткою і приберіть позначку TODO")
