# Multi-paradigm programming languages Lab2 Illia Pasichnichenko IKM-221a
print('Multi-paradigm programming languages Lab2')
print('Illia Pasichnichenko IKM-221a')


def get_float(var_name, default_message='Enter ', end_str=': '):
    try:
        user_input = float(input(default_message + var_name + end_str))
        return user_input
    except:
        print('It must be a number')
    return get_float(var_name, default_message, end_str)


def validate(value, condition_lambda, error_msg):
    while condition_lambda(value):
        value = get_float(error_msg)
    return value


x = get_float('x')
y = validate(get_float('y'), lambda _: _ == 12.4, 'the value cannot be equal to 12.4, enter again: ')
z = get_float('z')

result = (11 + 2 * x + 4.1) / (12.4 - y) + z
print(result)
