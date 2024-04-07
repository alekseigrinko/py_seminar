import random
from pathlib import Path

"""
Второе задание семинара, функция, которая генерирует псевдоимена.
Имя должно начиснаться с заглваной буквы,
состоять из 4-7 букв, среди которых обязательно должны быть гласные.
Полученные имена импортируются в файл
"""

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7


def random_names(filename: str | Path, count: int) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(count):
            name = ''
            cur_vowel = random.choice([-1, 1])
            for _ in range(random.randint(MIN_LEN, MAX_LEN)):
                if cur_vowel == 1:
                    name += random.choice(VOWELS)
                else:
                    name += random.choice(CONSONANTS)
                cur_vowel *= -1
            f.write(f'{name.title()}\n')


if __name__ == '__main__':
    random_names('names.txt', 100)
