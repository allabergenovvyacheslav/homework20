import math

def divide(first, second):
    try:
        result = first / second
    except ArithmeticError:
        result = math.inf
    return result