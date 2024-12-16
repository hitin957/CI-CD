def live_people():
    age_person = int(input("Введите возраст: "))
    year = 2023-age_person
    days = 0
    while year < 2023:
        if year % 4 == 0:
            days = days + 366
        else:
            days = days + 365
        year = year + 1
    return print("Вы прожили - ", days, "дней")
live_people()