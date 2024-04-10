import json
from pathlib import Path

"""
Напишите функцию, которая в бесконечном цмкле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключем имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""


def set_users(file: Path) -> None:
    u_ids = set()
    if not file.is_file():
        data = {i: {} for i in range(1, 8)}
    else:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for value in data.values():
            u_ids.update(value.keys())

    while True:
        name = input('Введите имя: ')
        if not name:
            break
        id = input('Введите id: ')
        lvl = input('Введите уровень доступа от 1 до 7: ')
        if ~(id in u_ids and data[lvl].get(id) is None):
            data[lvl].update({id: name})

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    set_users(Path('users.json'))
