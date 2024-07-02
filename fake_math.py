def divide(first, second):
    try:
        result = first / second
    except ArithmeticError:
        result = "Ошибка"
    return result