def get_float(var_name, default_message='Enter ', end_str=': '):
    try:
        user_input = float(input(default_message + var_name + end_str))
        return user_input
    except:
        print('It must be a number')
    return get_float(var_name, default_message, end_str)
