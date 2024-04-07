from random import randint, uniform
from pathlib import Path

"""
Первое задание семинара, функция, которая заполняет файл случайными парами чисел.
Первое число int, второе - float, разделены вертикальной числой.
Числа от -1000 до 1000
Количество строк - аргумент функции
"""

MIN_NUMBER = -1000
MAX_NUMBER = 1000


def fill_num(filename: str | Path, count: int) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(count):
            num_int = randint(MIN_NUMBER, MAX_NUMBER)
            num_float = uniform(MIN_NUMBER, MAX_NUMBER)
            f.write(f'{num_int}|{num_float}\n')


if __name__ == '__main__':
    fill_num(Path('numbers.txt'), 100)
