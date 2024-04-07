from pathlib import Path


# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри
# каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [1, 6] берутся буквы
# с 1 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.


def bulk_file_renaming(file_name: str = None, count_digit: int = None, extension_start: str = None,
                       extension_finish: str = None, range_name: list = None) -> None:
    """
    Функция переименования файлов. Для удобства в параметрах по умолчанию указано None.
    :param file_name: желаемое имя файла
    :param count_digit: количество символов в серийном номере файла
    :param extension_start: начальное расширения файла, по которому идет поиск в каталоге (в формате '.txt')
    :param extension_finish: конечное расширение файла, которое будет присмоено (в формате '.txt')
    :param range_name: колчиство символов, которое будет оставлено от исходного имени файла при переименовании
    """

    serial_number = 0

    for file in Path().cwd().iterdir():
        old_name = file.stem[range_name[0] - 1: range_name[1]]
        if file.suffix == extension_start:
            serial_number = create_serial_number(count_digit, serial_number)
            new_name = old_name + file_name + serial_number + extension_finish
            file.rename(Path().cwd() / new_name)


def create_serial_number(number_of_digits: int, last_number: str) -> str:
    """
    Функция принимает количество знаков в номере и последнее знаечние
    :param number_of_digits: количество знаков в номере
    :param last_number: последнее знаковое число в строковом выражении
    :return число, следующее за last_number в строковом выражении.
    """
    number = str(int(last_number) + 1)
    while len(number) <= number_of_digits - 1:
        number = '0' + number

    return number


if __name__ == '__main__':
    bulk_file_renaming('hw', 3, '.txt', '.bin', [1, 10])
