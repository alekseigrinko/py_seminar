import json
from pathlib import Path

"""
Вспоминаем задачу 3 из предыдущего семинара.
Напишите функцию, которая создает из ранее созданного файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""


def convert(file: Path) -> None:
    _dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split(' ')
            _dict[str(name).title()] = float(number)
    with open(f'{file.stem}.json', 'w', encoding='utf-8') as json_file:
        json.dump(_dict, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    convert(Path('results.txt'))
