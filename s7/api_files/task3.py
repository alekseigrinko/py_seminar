from pathlib import Path
from typing import TextIO

"""
Третье задание семинара, функция, которая открывает на чтение созданные ранее файлы.
Перемножьте пары чисел. В новый файл сохраните имя и произведение.
Если результат умножения отрицательный - сохраняется имя строчными буквами и произведение по модулю,
если положительный - сохраняется имя прописными буквами и произведение, округлённое до целого.
В результате в файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла - возвращается в его начало.
"""


def read_line_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.rstrip()


def convert_lines(names: str | Path, numbers: str | Path, results: str | Path) -> None:
    with (
        open(names, 'r', encoding='utf-8') as f_names,
        open(numbers, 'r', encoding='utf-8') as f_numbers,
        open(results, 'w', encoding='utf-8') as f_results
    ):
        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)
        max_len = max(len_names, len_numbers)
        for _ in range(max_len):
            name = read_line_or_begin(f_names)
            num_str = read_line_or_begin(f_numbers)
            num_i, num_f = map(float, num_str.split('|'))
            multiply = num_i * num_f
            if multiply < 0:
                f_results.write(f'{name.lower()} {-multiply}\n')
            elif multiply > 0:
                f_results.write(f'{name.upper()} {int(multiply)}\n')


if __name__ == '__main__':
    convert_lines(Path('names.txt'), Path('numbers.txt'), Path('results.txt'))
