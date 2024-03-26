import random

# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

_queen_list = []
MIN_ROW = 1
MIN_COL = 1
MAX_ROW = 8
MAX_COL = 8
MAX_QUEEN = 8  # изменить занчение константы для ввода необходимо количества фигур
LIST_ROW = [1, 2, 3, 4, 5, 6, 7, 8]
LIST_COL = [1, 2, 3, 4, 5, 6, 7, 8]
COUNT_SOLUTION = 4


def manual_start():
    """
    Запускает шахматный модуль для инициализации шахматных фигур в количестве, обозначенном переменной
    MAX_QUEEN
    :return: True, если полученные фигуры соответствуют условию задачи - не бьют друг друга
    """
    count = 0
    input_list = []
    while count < MAX_QUEEN:
        input_list.append(_input_queen(_manual_input()))
        count += 1
    print('Добавлены фигуры:')
    print(f'{input_list}')

    for item in input_list:
        if not _check_queen(item[0], item[1], _queen_list):
            print(f'Фигура на клетке: {item[0]}, {item[1]} подпадает под удар другой.')
            print('Нарушено условие задачи')
            _print_board(input_list)
            return False
        else:
            _queen_list.append(item)

    print('Расстановка фигур соответствует условию задачи!')
    _print_board(_queen_list)
    return True


def random_start():
    """
    Запускает шахматный модуль для инициализации шахматных фигур в количестве, обозначенном переменной
    MAX_QUEEN, для вывода использует случайный генератор чисел из списка LIST_ROW и LIST_COL
    :return: True, после вывода успешных решений в количестве константы COUNT_SOLUTION
    """
    count = 1

    while count <= COUNT_SOLUTION:

        check_list = []
        rows = LIST_ROW.copy()
        cols = LIST_COL.copy()
        count_queen = 1
        attempt_counter = 0

        while count_queen <= MAX_QUEEN and attempt_counter < 2:
            item = _input_queen(_random_input(rows, cols))
            if _check_queen(item[0], item[1], check_list):
                check_list.append(item)
                rows.remove(item[0])
                cols.remove(item[1])
                count_queen += 1
            else:
                attempt_counter += 1

            if check_list.__len__() == MAX_QUEEN:
                print(f'Расстановка фигур # {count} --->')
                _print_board(check_list)
                count += 1

    return True


def _input_queen(func_input):
    """
    Добавляет фигуру, координаты должны соответствовать параметрам MIN_ROW и MAX_ROW по горизонтали,
    MIN_COL и MAX_COL по вертикали,
    :return: пареметры row - горизонталь, col - вертикаль
    """
    while True:
        row, col = func_input
        if row < MIN_ROW or row > MAX_ROW or col < MIN_COL or col > MAX_COL:
            print('Некорректный формат ввода. Попробуйте еще раз.')
        else:
            break

    return row, col


def _manual_input():
    """
    Функция для ручного ввода параметров фигуры - использовалось в предыдущей версии
    :return: пареметры row - горизонталь, col - вертикаль
    """
    row = int(input(f'Введите строку в диапозоне {MIN_ROW} - {MAX_ROW}: '))
    col = int(input(f'Введите столбец {MIN_COL} - {MAX_COL}: '))
    return row, col


def _random_input(list_row, list_col):
    """
    Функция для произвольного ввода параметров фигуры из списков допустимых значений по горизонтали и вертикали
    :return: пареметры row - горизонталь, col - вертикаль
    """
    row = random.choice(list_row)
    col = random.choice(list_col)
    return row, col


def _check_queen(row, col, check_list: list):
    """
    Функция проверки фигуры на соответствие условию задачи, т.е. имеется ли уже введенная фигура,
    которая бьет проверяемую в обозанченном списке
    :return: True, если фигугра не бьется имеющимися, False - фигура не соответствует условию
    """
    count = 0
    for queen in check_list:
        if row == queen[0] or col == queen[1] or row + col == queen[0] + queen[1] \
                or row - col == queen[0] - queen[1]:
            count += 1
            if count > 1:
                return False

    if count == 0:
        return True


def _print_board(check_list: list):
    """
    Функция вывода введенной растановки фигур на доске в консоль
    """
    for i in range(1, MAX_ROW + 1):
        print_list = []
        for j in range(1, MAX_COL + 1):
            if (i, j) in check_list:
                print_list.append('|Q|')
            else:
                print_list.append('|_|')
        print(''.join(print_list))


if __name__ == '__main__':
    random_start()
