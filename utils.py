import re


def get_float(var_name, default_message='Enter ', end_str=': '):
    try:
        user_input = float(input(default_message + var_name + end_str))
        return user_input
    except ValueError:
        print('It must be a number')
    return get_float(var_name, default_message, end_str)


def validate(value, condition_lambda, error_msg):
    while condition_lambda(value):
        value = get_float(error_msg, '')
    return value


def get_number(message, expected_type):
    user_input = input(message)
    try:
        converted_input = expected_type(user_input)
        return converted_input
    except ValueError:
        print(f'The value must be of type {expected_type.__name__}')
        return get_number(message, expected_type)


def get_reg_ex_input(message, pattern, err_message='invalid input, try again', ):
    while True:
        user_input = input(message)

        if not re.match(pattern, user_input):
            print(err_message)
            continue

        return user_input
