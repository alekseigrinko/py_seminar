import json
import pickle
from pathlib import Path

"""
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноименных
pickle файлов.
"""


def json_to_pickle(path: Path) -> None:
    for file in path.iterdir():
        if file.is_file() and file.suffix == '.json':
            with open(file, 'r', encoding='utf-8') as f_read:
                data = json.load(f_read)
            with open(file.with_suffix('.pickle'), 'wb') as f_write:
                pickle.dump(data, f_write)


if __name__ == '__main__':
    json_to_pickle(Path.cwd())
