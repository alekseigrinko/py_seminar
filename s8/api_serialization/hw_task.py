from pathlib import Path
import json
import pickle
import csv


# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
# с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.


def travel_to_directory(directory: Path) -> list:
    """
    Функция проходит рекурсивно по всей и директории и вложенным папкам и предоставляет информацию по дереву каталога
    :param directory: директория, по которой будет собираться информация
    :return: список файлов и директорий
    """
    tree_list = []
    for file in directory.iterdir():
        if file.is_dir():
            tree_list.append(f'{file} - директория, размер директории - {_size_of_directory(file)} байт, '
                             f'родительская директория - {file.parent}')
            tree_list.extend(travel_to_directory(file))
        elif file.is_file():
            tree_list.append(f'{file} - файл, размер файла - {file.stat().st_size} байт')

    result_file = Path(Path.cwd() / Path(f'{Path.cwd().stem}_tree.json'))

    with open(result_file, 'w', encoding='utf-8') as json_write:
        json.dump(tree_list, json_write, ensure_ascii=False, indent=4)
    with open(result_file.with_suffix('.pickle'), 'wb') as pickle_write:
        pickle.dump(tree_list, pickle_write)
    with open(result_file.with_suffix('.csv'), 'w', encoding='utf-8') as csv_write:
        writer = csv.writer(csv_write, delimiter='\n')
        writer.writerow(tree_list)

    return tree_list


def _size_of_directory(_dir: Path) -> bytes:
    """
    Функция возвращает размер директории в байтах
    :param _dir: директория запроса
    :return: размер директории
    """
    count_byte = 0
    for file in _dir.iterdir():
        if file.is_dir():
            count_byte += _size_of_directory(file)
        elif file.is_file():
            count_byte += file.stat().st_size
    return count_byte


if __name__ == "__main__":
    travel_to_directory(Path.cwd())
