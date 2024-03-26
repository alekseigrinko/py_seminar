from datetime import datetime


# Модуль с проверкой даты


def check_date(date: str) -> bool:
    """
    Проверяет, является ли строка дата в формате DD.MM.YYYY
    :param date: строка дата в формате DD.MM.YYYY
    :return: True, если строка дата в формате DD.MM.YYYY
    """
    try:
        datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        return False


def input_date(*args):
    """
    Проверяет, является ли введенные аргументы (по-умолчанию через терминал)
    датой в формате DD.MM.YYYY
    :param набор аргументов, где передена строка дата в формате DD.MM.YYYY
    :return: True, если в составе аргументов - строка дата в формате DD.MM.YYYY
    """
    _list = list(*args)
    print(_list)
    if check_date(_list[1]):
        print('Дата в формате DD.MM.YYYY')
    else:
        print('Дата не в формате DD.MM.YYYY')


if __name__ == '__main__':
    date = input('Введите дату в формате DD.MM.YYYY: ')
    if check_date(date):
        print('Дата в формате DD.MM.YYYY')
    else:
        print('Дата не в формате DD.MM.YYYY')
