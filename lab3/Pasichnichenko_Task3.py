from math import sin, atan


def get_float(message):
    try:
        user_input = float(input(message))
        if isinstance(user_input, float):
            return user_input
    except:
        print('It must be a number')
        return get_float(message)


def get_not_equal_to_0_number(number_to_validate):
    while number_to_validate == 0:
        number_to_validate = get_float('the number cannot be equal to 0, try again: ')
    return float(number_to_validate)


# Multi-paradigm programming languages Lab2 Illia Pasichnichenko IKM-221a
print('Multi-paradigm programming languages Lab2')
print('Illia Pasichnichenko IKM-221a')

a = get_not_equal_to_0_number(get_float('Enter a value: '))
b = get_not_equal_to_0_number(get_float('Enter b value: '))
c = get_not_equal_to_0_number(get_float('Enter c value: '))

y = (sin(2 * a) / a - 3) + (atan(b) / c)

print(y)
