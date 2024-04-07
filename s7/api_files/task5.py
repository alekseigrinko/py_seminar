from task4 import create_files

"""
Пятое задание семинара, функция, которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве аргуметов.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
"""


def generate_file(**kwargs) -> None:
    for extension, amount in kwargs.items():
        create_files(extension, count=amount)


if __name__ == '__main__':
    generate_file(bin=0, jpg=0, txt=3)
