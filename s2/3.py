import fractions
import math

# Напишите программу, которая принимает две строки вида
# “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

def make_example():
    f_1 = str(input('Введите первую дробь вида a/b: '))
    while True:
        if (f_1.__len__() == 3):
            if  f_1[0].isdigit() and f_1[2].isdigit() and int(f_1[2]) > 0 and f_1[1] == '/':
                break
            else:
                print('Некорректный формат ввода. Попробуйте еще раз.')
                f_1 = str(input('Введите первую дробь вида a/b: '))
        else:
            print('Некорректный формат ввода. Попробуйте еще раз.')
            f_1 = str(input('Введите первую дробь вида a/b: '))

    f_2 = str(input('Введите вторую дробь вида a/b: '))
    while True:
        if (f_2.__len__() == 3):
            if  f_2[0].isdigit() and f_2[2].isdigit() and int(f_2[2]) > 0 and f_2[1] == '/':
                break
            else:
                print('Некорректный формат ввода. Попробуйте еще раз.')
                f_2 = str(input('Введите вторую дробь вида a/b: '))
        else:
            print('Некорректный формат ввода. Попробуйте еще раз.')
            f_2 = str(input('Введите вторую дробь вида a/b: '))
    print(f'Вы ввели: {f_1}, {f_2}')
    sum_of_fractions(f_1, f_2)
    multiply_fractions(f_1, f_2)

def sum_of_fractions(f_1, f_2):
    a_1, a_2, b_1, b_2 = convert_fraction(f_1, f_2)

    numerator = a_1 * b_2 + b_1 * a_2
    denominator = a_2 * b_2

    print(f'Значение суммы дробей: {reduction_fraction(numerator, denominator)}')
    print(f'Проверка значения через модуль fractions: {fractions.Fraction(f_1) + fractions.Fraction(f_2)}')

def multiply_fractions(f_1, f_2):
    a_1, a_2, b_1, b_2 = convert_fraction(f_1, f_2)

    numerator = a_1 * b_1
    denominator = a_2 * b_2

    print(f'Значение произведения дробей: {reduction_fraction(numerator, denominator)}')
    print(f'Проверка значения через модуль fractions: {fractions.Fraction(f_1) * fractions.Fraction(f_2)}')

def convert_fraction(f_1, f_2):
    return int(f_1[0]), int(f_1[2]), int(f_2[0]), int(f_2[2])

def reduction_fraction(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    while gcd > 1:
        numerator //= gcd
        denominator //= gcd
        gcd = math.gcd(numerator, denominator)

    if denominator == 1:
        return numerator
    else:
        return f'{numerator}/{denominator}'

make_example()