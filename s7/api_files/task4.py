from random import randint, choices
from string import ascii_lowercase, digits

"""
Четвертое задание семинара, функция, которая создает файлы с указанным расширением.
Функция принимает следующие параметры - расширение, минимальная длина случайно сгенерированного имени,
по умолчанию 6, максимальная длина случайно сгенерированного имени, по умолчанию 30,
минимальное число случайных байт, записанных в файл, по умолчанию 256, максимальное число случайных байт,
записанных в файл, по умолчанию 4096.
Количество файлов, по умолчанию 42.
Имя файла и его размер должны быть в рамках переданного диапозона.
"""


def create_files(extension: str, min_len: int = 6, max_len: int = 30, min_size: int = 256, max_size: int = 4096,
                 count: int = 42) -> None:
    for _ in range(count):
        name = ''.join(choices(ascii_lowercase + digits, k=randint(min_len, max_len)))
        size = randint(min_size, max_size)
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(b'\0' * size)


if __name__ == '__main__':
    create_files('txt', count=1)