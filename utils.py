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


def get_number(var_name, expected_type=float):
    user_input = input(f'Enter {var_name}: ')
    try:
        converted_input = expected_type(user_input)
        return converted_input
    except ValueError:
        print(f'The value must be of type {expected_type.__name__}')
        get_number(var_name, expected_type)
