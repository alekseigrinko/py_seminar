
# Создайте функцию генератор чисел Фибоначчи

def make_example():
    while True:
        n = input('Введите размер последовательности чисел Фибоначчи: ')
        if n.isdigit():
            n = int(n)
            break
        else:
            print('Некорректный формат ввода. Попробуйте еще раз.')

    for i in fibonacci(n):
        print(i)


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


make_example()
