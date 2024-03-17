# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
import decimal


def make_example():
    LIMIT_WEIGHT = 100
    backpack_dict = get_items(LIMIT_WEIGHT)
    print(f'Подготовлен перечень вещей в поход {backpack_dict = }')
    # в переменную COUNT нужно указать количество вариантов комплекта
    # рекомендуется до 20, далее лучше доработать код
    some_fill_backpack(backpack_dict, LIMIT_WEIGHT,20)

def get_items(LIMIT_WEIGHT):
    backpack_dict = {}

    print("Введите название вещи, вес которого добавляем в рюкзак в кг."\
          " Или введите 'default' в название вещи\n"\
          f"Всего можно добавить пять наименований, лимит веса - {LIMIT_WEIGHT}:")
    count = 5
    while count > 0:
        item = str(input('Введите название вещи: '))
        if item == 'default':
            backpack_dict = get_default()
            break
        try:
            weight = float(input('Введите вес: '))
        except ValueError:
            print('Некорректный формат ввода. Попробуйте еще раз.')
            continue
        if sum(backpack_dict.values()) > LIMIT_WEIGHT or weight > LIMIT_WEIGHT:
            print(f'Отсутствует максимальная грузоподъёмность для вещей.')
            count = 0
        else:
            backpack_dict[item] = weight
            print(f'Вещь {item} добавлена с весом {weight}.')
            count -= 1

    return backpack_dict

def get_default():
    return {"куртка": 5.0, "ботинки": 2.5, "бутылка воды": 1.0, "тущенка": 0.5, "шоколадка": 0.1}

def fill_backpack_one(backpack_dict, LIMIT_WEIGHT): # один вариант комплектации рюкзака
    items_dict = sorted(backpack_dict.items(), key=lambda x: x[1], reverse=True)
    limit = LIMIT_WEIGHT
    final_dict = {}
    while True:
        for item, weight in items_dict:
            if weight <= limit:
                if item not in final_dict:
                    final_dict[item] = 1
                else:
                    final_dict[item] += 1
                limit = round((limit - weight), 2)
            else:
                limit = round((limit - 0), 2)
        if items_dict[-1][1] > limit:
            break

    print(f'Вариант комплектации рюкзака:\n{final_dict}\nОстаток лимита веса - {round(limit, 2)} кг.')

    return final_dict, limit

def some_fill_backpack(backpack_dict, LIMIT_WEIGHT, COUNT): # несколько вариантов комплектации рюкзака
    # в переменную COUNT нужно указать количество вариантов комплекта
    items_dict = sorted(backpack_dict.items(), key=lambda x: x[1], reverse=True)
    limit = LIMIT_WEIGHT
    final_dict = {}
    while True:
        for i in range(len(items_dict)):
            item, weight = items_dict[i]
            if weight <= limit:
                if item not in final_dict:
                    final_dict[item] = 1
                else:
                    final_dict[item] += 1
                limit = round((limit - weight), 2)
            else:
                limit = round((limit - 0), 2)
        if items_dict[-1][1] > limit:
            break

    print(f'Вариант 1 комплектации рюкзака:\n{final_dict}\nОстаток лимита веса - {round(limit, 2)} кг.')

    steps = [1, 0, 0]
    count = COUNT - 1
    reverse = True
    while count > 0:
        intermediate_dict = {}
        limit = LIMIT_WEIGHT
        while True:
            for i in range(len(items_dict)):
                item, weight = items_dict[i]
                if weight <= limit:
                    if item not in intermediate_dict:
                        intermediate_dict[item] = 1
                        limit = round((limit - weight), 2)
                    elif not ((i == 0 and intermediate_dict[item] >= final_dict[item] - steps[i]) \
                          or (i == 1 and intermediate_dict[item] >= final_dict[item] - steps[i])\
                            or (i == 2 and intermediate_dict[item] >= final_dict[item] - steps[i])):
                        intermediate_dict[item] += 1
                        limit = round((limit - weight), 2)
                    else:
                        limit = round((limit - 0), 2)
                else:
                    limit = round((limit - 0), 2)
            if items_dict[-1][1] > limit:
                break

        if (steps[0] > steps[1]):
            steps[1] += 1
        elif not (intermediate_dict[items_dict[0][0]] == 1 and intermediate_dict[items_dict[1][0]] == 1):
            steps[0] += 1
        else:
            steps[2] += 1

        if reverse and (intermediate_dict[items_dict[0][0]] == 1 or intermediate_dict[items_dict[1][0]] == 1):
            final_dict = intermediate_dict
            reverse = False

        count -= 1
        print(f'Вариант {COUNT - count} комплектации рюкзака:\n{intermediate_dict}\nОстаток лимита веса - {round(limit, 2)} кг.\n')

        if intermediate_dict[items_dict[2][0]] == 1:
            print('Для текущей версии варианты закончились')
            break

make_example()