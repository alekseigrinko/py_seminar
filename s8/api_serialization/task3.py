from pathlib import Path
import csv
import json

"""
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV
"""


def json_to_csv(file: Path) -> None:
    with open(file, 'r', encoding='utf-8') as f_read:
        data = json.load(f_read)

    list_rows = []
    for level, id_name_dict in data.items():
        for id, name in id_name_dict.items():
            list_rows.append({'level': int(level), 'id': int(id), 'name': name})

    with open(file.with_suffix('.csv'), 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(list_rows)


if __name__ == '__main__':
    json_to_csv(Path('users.json'))
