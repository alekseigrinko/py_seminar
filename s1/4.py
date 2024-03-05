import random

# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

def make_example():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    num = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    attempt = 10

    print('Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.')

    while attempt > 0:
        print(f'У Вас осталось {attempt} попыток!')
        guess = int(input('Введите число от 0 до 1000: '))

        if guess < num:
            print('\nБольше\n')
            attempt -= 1

        elif guess > num:
            print('\nМеньше\n')
            attempt -= 1

        else:
            print('\nПравильно')
            print(f'Вы угадали число {num}')
            break

    if attempt == 0:
        print('\nПопытки закончились!')
        print(f'Вы не угадали число {num}')

make_example()