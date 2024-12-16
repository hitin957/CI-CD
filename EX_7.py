def convert_value(value, data_type):
    try:
        if data_type == int:
            return int(value)
        elif data_type == float:
            return float(value)
        elif data_type == bool:
            return bool(value)
        elif data_type == str:
            return str(value)
        elif data_type == list:
            return list(value)
        else:
            return None
    except (ValueError, TypeError):
        print(f"Ошибка преобразования значения {value} в тип {data_type.__name__}")
print(convert_value("123", int))
print(convert_value("3.14", float))
print(convert_value("True", bool))
print(convert_value(123, str))
print(convert_value("1,2,3", list))
print(convert_value("abc", int))