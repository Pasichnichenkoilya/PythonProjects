from math import sin, atan


def get_float(var_name, default_message='Enter ', end_str=': '):
    try:
        user_input = float(input(default_message + var_name + end_str))
        return user_input
    except:
        print('It must be a number')
    return get_float(var_name, default_message, end_str)


def validate(value, condition_lambda, error_msg):
    while condition_lambda(value):
        value = get_float(error_msg, '')
    return value


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
