# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление

def make_example():
    HEX = 16

    num = int(input('Введите целое число: '))
    result: str = ""
    test_num = num
    while test_num > 0:
        match test_num % HEX:
            case 10:
                result = "a" + result
            case 11:
                result = "b" + result
            case 12:
                result = "c" + result
            case 13:
                result = "d" + result
            case 14:
                result = "e" + result
            case 15:
                result = "f" + result
            case _:
                result = str(test_num % HEX) + result

        test_num //= HEX

    print("Получилось значение в шестнадцатеричной системе: 0x" + result)
    print(f"Проверка значения: {hex(num) = }")

make_example()