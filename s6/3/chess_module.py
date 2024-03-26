
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

_queen_list = []
MIN_ROW = 1
MIN_COL = 1
MAX_ROW = 8
MAX_COL = 8
MAX_QUEEN = 3  # изменить занчение константы для ввода необходимо количества фигур


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
        if not _check_queen(item[0], item[1]):
            print(f'Фигура на клетке: {item[0]}, {item[1]} подпадает под удар другой.')
            print('Нарушено условие задачи')
            _print_board(input_list)
            return False
        else:
            _queen_list.append(item)

    print('Расстановка фигур соответствует условию задачи!')
    _print_board(_queen_list)
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
    Функция для ручного ввода параметров фигуры
    :return: пареметры row - горизонталь, col - вертикаль
    """
    row = int(input(f'Введите строку в диапозоне {MIN_ROW} - {MAX_ROW}: '))
    col = int(input(f'Введите столбец {MIN_COL} - {MAX_COL}: '))
    return row, col


def _check_queen(row, col):
    """
    Функция проверки фигуры на соответствие условию задачи, т.е. имеется ли уже введенная фигура,
    которая бьет проверяемую
    :return: True, если фигугра не бьется имеющимися, False - фигура не соответствует условию
    """
    count = 0
    for queen in _queen_list:
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
    manual_start()

