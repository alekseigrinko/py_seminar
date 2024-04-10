from pathlib import Path
import csv
import json

"""
Прочитайте созданный в прошлом задании файл без использования csv.DictReader.
Дополните id до 10 цифр незначащимися нулями.
В именах сделайте первую букву прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраниет в json файл, где кажая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файла передаются как аргументы функции.
"""


def csv_to_json(csv_file: Path, json_file: Path) -> None:
    json_list = []
    with open(csv_file, 'r', encoding='utf-8') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_read):
            json_dict = {}
            if i != 0:
                level, id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = f'{int(id):010}'
                json_dict['name'] = name
                json_dict['hash'] = hash(f'{json_dict["name"]}{json_dict["id"]}')
                json_list.append(json_dict)
    with open(json_file, 'w', encoding='utf-8') as f_write:
        json.dump(json_list, f_write, indent=4)


if __name__ == '__main__':
    csv_to_json(Path('users.csv'), Path('new_users.json'))
