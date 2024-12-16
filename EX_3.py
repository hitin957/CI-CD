def search_stroka(search, stroka):
    return print("Количество встреч первой строки со второй ", stroka.count(search))
stroka = str(input("Введите строку: "))
search = str(input("Введите строку которую хотите найти: "))
search_stroka(search=search, stroka=stroka)