"""
Формирование списка заданных по условию имен:
- remove_double_symbol - удаление повторяющихся подряд символов в слове
- get_list_without_double - получение списка слов без дублей
- get_names_list - получение списка имен одинаковой длинны
"""

# Если по условию исключено дублирование любых символов в имени файла
# необхдимо использовать закомментированную функцию
# def remove_double_symbol(word):
#     from collections import OrderedDict
#     return ''.join(OrderedDict.fromkeys(word))

def remove_double_symbol(word):
    if len(word) == 1:
        return word
    else:
        clean_word, last_letter = '', None
        for letter in word:
            if last_letter == letter:
                continue
            else:
                clean_word += letter
                last_letter = letter
        return clean_word


def get_list_without_double(names_list):
    return list(set([remove_double_symbol(i) for i in names_list
                     if isinstance(i, str) and len(i) > 0]))


def get_names_list(names_list):
    cleaned_names_list = get_list_without_double(names_list)
    result = []
    max_len_word = len(max(cleaned_names_list, key=len))
    for title in cleaned_names_list:
        if len(title) != max_len_word:
            result.append(title + '_' * (max_len_word - len(title)))
        else:
            result.append(title)
    return result

