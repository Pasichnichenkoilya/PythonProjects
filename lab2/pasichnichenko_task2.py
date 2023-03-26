from utils import get_float, validate

# Multi-paradigm programming languages Lab2 Illia Pasichnichenko IKM-221a
print('Multi-paradigm programming languages Lab2')
print('Illia Pasichnichenko IKM-221a')


def equal_to_twelve_point_four(value):
    return value == 12.4


TWELVE_POINT_FOUR_ERROR = 'the value cannot be equal to 12.4, enter again'

x = get_float('x')
y = get_float('y')
y = validate(y, equal_to_twelve_point_four, TWELVE_POINT_FOUR_ERROR)
z = get_float('z')

result = (11 + 2 * x + 4.1) / (12.4 - y) + z
print(result)
