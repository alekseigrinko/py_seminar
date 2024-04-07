from random import randint, choices
from string import ascii_lowercase, digits
from pathlib import Path
from os import chdir

"""
Шестое задание семинара, функция, которая генерирует файлы в указанную директорию - 
отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имен.
"""


def create_files(extension: str, min_len: int = 6, max_len: int = 30, min_size: int = 256, max_size: int = 4096,
                 count: int = 42) -> None:
    for _ in range(count):
        chdir(Path.cwd())
        while True:
            name = ''.join(choices(ascii_lowercase + digits, k=randint(min_len, max_len)))
            if not Path(f'{name}.{extension}').is_file():
                break
        size = randint(min_size, max_size)
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(b'\0' * size)


def generate_file(filepath: str | Path, **kwargs) -> None:
    if isinstance(filepath, str):
        filepath = Path(filepath)
    if not filepath.is_dir():
        filepath.mkdir(parents=True)
    chdir(filepath)
    for extension, amount in kwargs.items():
        create_files(extension, count=amount)


if __name__ == '__main__':
    generate_file(Path.cwd() / 'files', txt=1)
