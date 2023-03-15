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


def get_int(var_name, default_message='Enter ', end_str=': '):
    try:
        user_input = int(input(default_message + var_name + end_str))
        return user_input
    except ValueError:
        print('It must be an integer')
    return get_int(var_name, default_message, end_str)
