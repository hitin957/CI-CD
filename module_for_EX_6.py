def Search_for_a_character_in_the_prescribed_string(stroka:str, char:chr):
    return print("результат поиска символа в прописанной строке",char in stroka)
def Return_the_list_of_capital_letters(stroka:str):
    list=[]
    for i in stroka:
        if i.isupper():
            list.append(i)
    return print("Список заглавных букв: ", list)
def Return_a_list_of_lowercase_letters(stroka:str):
    list = []
    for i in stroka:
        if i.islower():
            list.append(i)
    return print("Список прописных букв: ", list)
def Return_a_list_of_numeric_characters(stroka:str):
    list = []
    for i in stroka:
        if i.isnumeric():
            list.append(i)
    return print("Список числовых символов: ", list)
def Checking_the_symbol_for_belonging_to_capital_letters(char:chr):
    return print("Проверка символа на принадлежность к заглавным буквам: ", char.isupper())
def Checking_the_character_for_belonging_to_lowercase_letters(char:chr):
    return print("Проверка символа на принадлежность к строчным буквам: ", char.islower())
def Checking_the_symbol_for_belonging_to_numbers(char:chr):
    return print("Проверка символа на принадлежность к цифрам: ", char.isnumeric())
def Counting_substrings_in_the_specified_string(stroka:str, under_stroka:str):
    return print("Подсчет подстрок в указанной строке: ", stroka.count(under_stroka))