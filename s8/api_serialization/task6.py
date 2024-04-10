import pickle
import csv
from pathlib import Path

"""
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестирования возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря из заголовков столбца из переданного файла.
"""


def pickle_to_csv(pickle_file: Path, csv_file: Path) -> None:
    with open(pickle_file, 'rb') as f_read:
        data = pickle.load(f_read)
    with open(csv_file, 'w', newline='', encoding='utf-8') as f_write:
        writer = csv.DictWriter(f_write, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    pickle_to_csv(Path('new_users.pickle'), Path('new_users_2.csv'))
