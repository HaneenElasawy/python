import math

def calculate_area(shape, x, y=0):
    if shape == 't':
        return 0.5 * x * y

    elif shape == 'r':
        return x * y

    elif shape == 's':
        return x * x

    elif shape == 'c':
        return math.pi * (x ** 2)

    else:
        return "Invalid shape"


print(calculate_area('t', 10, 7))
print(calculate_area('r', 10, 7))
print(calculate_area('s', 10))
print(calculate_area('c', 10))