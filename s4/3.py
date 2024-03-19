# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_PRINT = 'о'
CMD_QUIT = 'в'
RICHNESS_SUM = 5_000_000
RICHNESS_TAX = 10 / 100
WITHDRAW_PERCENT = 15 / 1000
ADD_PERCENT = 3 / 100
MULTIPLICITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3
operation_list = []


def make_example():
    account = float(0)
    count = 0

    while True:
        if account > RICHNESS_SUM:
            account = withhold_tax(account)

        command = input(f'Пополнить - {CMD_DEPOSIT}, Снять - {CMD_WITHDRAW}, Список операций - {CMD_PRINT}, '
                        f'Выйти - {CMD_QUIT}: ')

        if command == CMD_QUIT:
            print(f'Возьмите карту, на которой {account} у.е.')
            break

        if command == CMD_PRINT:
            print_operation_list()

        if command in (CMD_DEPOSIT, CMD_WITHDRAW):
            amount = 1
            while amount % 50 != 0:
                amount = int(input(f'Введите сумму кратную {MULTIPLICITY}: '))

        if command == CMD_DEPOSIT:
            account, count = deposit(account, amount, count)

        if command == CMD_WITHDRAW:
            account, count = withdraw(account, amount, count)

        if count and count % COUNT_OPER == 0:
            account = get_bonus(account)


def deposit(account, amount, count):
    account += amount
    count += 1
    message = (f'Пополнение карты на {amount} у.е.\n')
    print(message + f'Итого на карте: {account} у.е.')

    operation_list.append(message)

    return account, count


def withdraw(account, amount, count):
    withdraw_tax = amount * WITHDRAW_PERCENT
    withdraw_tax = (MIN_REMOVAL if amount < MIN_REMOVAL else
                    MAX_REMOVAL if amount > MAX_REMOVAL else withdraw_tax)

    if account >= amount + withdraw_tax:
        count += 1
        account -= amount + withdraw_tax
        message = (f'Снятие с карты {amount} у.е.\nКомиссия за снятие {withdraw_tax} у.е.\n')
        print(message + f'Итого на карте: {account} у.е.')
    else:
        message = (f'Недостаточно денег для выполнения операции.\n'
                   f'Затребовая сумма: {amount} у.е., Комиссия составила {withdraw_tax} у.е.\n')
        print(message + f'Итого на карте: {account} у.е.')

    operation_list.append(message)

    return account, count


def get_bonus(account):
    bonus_percent = account * ADD_PERCENT
    account += bonus_percent
    message = (f'На счет начислено {ADD_PERCENT * 100}%, составляющие {bonus_percent}у.е.\n')
    print(message + f'Итого на карте {account} у.е.')

    operation_list.append(message)

    return account


def withhold_tax(account):
    percent = account * RICHNESS_TAX
    account -= percent
    message = (f'Удержан налог на богатство {RICHNESS_TAX * 100}% в ра��зере {percent} у.е.\n')
    print(message + f'Итого на карте: {account} у.е.')

    operation_list.append(message)

    return account


def print_operation_list():
    if len(operation_list) == 0:
        print('Список операций пуст.')
    else:
        for i, operation in enumerate(operation_list):
            print(f'{i + 1}: {operation}')


make_example()
