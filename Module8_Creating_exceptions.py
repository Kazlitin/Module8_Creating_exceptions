class InvalidDataException(Exception):
    """Исключение, которое генерируется, когда данные некорректны."""
    pass

class ProcessingException(Exception):
    """Исключение, которое генерируется, когда процессор не может обработать данные."""
    pass

def generate_exceptions(arg1, arg2):
    """Функция, которая генерирует исключения в зависимости от аргументов."""
    if arg1 > arg2:
        raise InvalidDataException("Аргумент 1 больше аргумента 2")
    elif arg1 == arg2:
        raise ProcessingException("Аргументы равны друг другу")
    else:
        return None  # Если исключение не сгенерировано, возвращаем None

try:
    # Вызов функции с различными аргументами
    generate_exceptions(10, 5)
    generate_exceptions(5, 5)
    generate_exceptions(5, 10)
except InvalidDataException as e:
    print(f"Обработка исключения InvalidDataException: {e}")
except ProcessingException as e:
    print(f"Обработка исключения ProcessingException: {e}")
else:
    print("Никаких исключений не было сгенерировано.")
finally:
    print("Это блок 'finally', он выполняется всегда после блока 'try'")