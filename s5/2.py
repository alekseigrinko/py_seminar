import os.path

# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Пример абсолютного пути - C:\user\docs\Letter.txt

def make_example():
    while True:
        path = input('Введите абсолютный путь или введите 0 для ввода занчения по умолчанию: ')
        if path == '0':
            path = "C:/user/docs/Letter.txt"

        if os.path.isabs(path):
            break
        else:
            print('Некорректный формат ввода. Попробуйте еще раз.')

    result = convert(path)

    print(f'Переданный абсолютный путь - {path}')
    print(f'Путь к файлу - {result[0]}')
    print(f'Переданное имя файла - {result[1]}')
    print(f'Переданное расширение файла - {result[2]}')


def convert(path):
    path_split = os.path.split(path)
    if '.' in path_split[1]:
        file_name, file_extension = path_split[1].split('.')
    else:
        file_name = path_split[1]
        file_extension = 'отсутствует расширение файла'

    return path_split[0], file_name, file_extension


make_example()