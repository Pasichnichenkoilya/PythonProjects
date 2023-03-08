# Multi-paradigm programming languages Lab2 Illia Pasichnichenko IKM-221a
print('Multi-paradigm programming languages Lab2')
print('Illia Pasichnichenko IKM-221a')


def get_float(message):
    try:
        user_input = float(input(message))
        if isinstance(user_input, float):
            return user_input
    except:
        print('It must be a number')
        return get_float(message)


x = get_float('Enter x: ')
y = get_float('Enter y: ')
z = get_float('Enter z: ')

result = (11 + 2 * x + 4.1) / (12.4 - y) + z

print(result)
