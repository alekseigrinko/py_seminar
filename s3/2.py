import random

# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

def make_example():
    new_list = create_list(15)
    list_without_duplicates = list(set(new_list))
    list_duplicates = []

    for i in list_without_duplicates:
        if new_list.count(i) > 1:
            list_duplicates.append(i)

    list_not_duplicates = list(set(list_without_duplicates) - set(list_duplicates))

    print(f'Первоначальный список: {new_list}')
    print(f'Список без повторяющихся элементов: {list_without_duplicates}')
    print(f'Список повторяющихся элементов: {list_duplicates}')
    print(f'Список не повторяющихся элементов: {list_not_duplicates}')


def create_list(length):
    LOWER_LIMIT = 1
    UPPER_LIMIT = 10
    num = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    new_list = []
    for i in range(length):
        new_list.append(num)
        num = random.randint(LOWER_LIMIT, UPPER_LIMIT)

    return new_list

make_example()