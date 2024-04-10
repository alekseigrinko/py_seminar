import csv
import pickle
from pathlib import Path

"""
Прочитайте созданный в предыдущем задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
"""


def csv_to_pickle(csv_file: Path) -> None:
    pickle_list = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_read):
            print(i, line)
            if i == 0:
                pickle_keys = line
            else:
                pickle_dict = {k: v for k, v in zip(pickle_keys, line)}
                pickle_list.append(pickle_dict)
    print(pickle.dumps(pickle_list))


if __name__ == '__main__':
    csv_to_pickle(Path('users.csv'))
