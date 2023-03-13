from math import sin, atan
from utils import get_float, validate


def equal_to_zero(value):
    return value == 0


# Multi-paradigm programming languages Lab2 Illia Pasichnichenko IKM-221a
print('Multi-paradigm programming languages Lab2')
print('Illia Pasichnichenko IKM-221a')

equal_to_zero_msg = 'the value cannot be equal to zero'

a = validate(get_float('a'), equal_to_zero, equal_to_zero_msg)
b = validate(get_float('b'), equal_to_zero, equal_to_zero_msg)
c = validate(get_float('c'), equal_to_zero, equal_to_zero_msg)

y = (sin(2 * a) / a - 3) + (atan(b) / c)
print(y)
