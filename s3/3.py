import wikipedia
# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

def make_example():
    words_list = count_words(convert_string(get_article()))
    print("Список часто повторяющихся слов статьи Википедии по запросу Дзен Пайтона:\n")
    for word in words_list:
        print(f"{word[0]} - {word[1]} повторений")

def convert_string(string):
    str_elements = string.lower().split(' ')
    new_str_elements = []
    for elem in str_elements:
        if not elem.isalpha():
            for char in elem:
                if not char.isalpha():
                    elem = elem.replace(char, "")
        if elem:
            new_str_elements.append(elem)

    return new_str_elements

def get_article():
    language = "ru"
    wikipedia.set_lang(language)
    return wikipedia.summary("Дзен Пайтона")

def count_words(string):
    new_dict = {}
    for word in string:
        if word in new_dict:
            new_dict[word] += 1
        else:
            new_dict[word] = 1

    sort_dict = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)

    sort_list = []

    for i in range(10):
        sort_list.append(sort_dict[i])

    return sort_list

make_example()
