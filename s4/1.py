import random


# Напишите функцию для транспонирования матрицы


def make_example():
    matrix = create_matrix()
    print(f'Первичная матрица: {matrix}')
    print(f'Транспонированная матрица: {transpose_matrix(matrix)}')


def create_num():
    """ генерация числа от 1 до 10 """
    return random.randint(1, 10)


def create_matrix():
    """ генерация 3x3 матрицы """
    matrix = []
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(create_num())
    return matrix


def transpose_matrix(matrix):
    """ транспонирование матрицы """
    return list((list(row) for row in zip(*matrix)))


make_example()
