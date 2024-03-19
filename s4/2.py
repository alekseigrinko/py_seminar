# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def make_example():
    print(create_dict(a=1, b=2, c=3))


def create_dict(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        new_dict[value] = key

    return new_dict


make_example()
