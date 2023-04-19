import re
from utils import get_number


def to_binary(decimal_value: int) -> str:
    binary = ''
    while decimal_value:
        binary += str(decimal_value % 2)
        decimal_value //= 2
    return binary[::-1]


def to_decimal(binary_value: str) -> float:
    decimal = 0
    power = 0
    for i in reversed(range(len(binary_value))):
        digit = int(binary_value[i])
        decimal += digit * 2 ** power
        power += 1
    return decimal


covert_to_binary = get_number('Enter 0 to convert decimal to binary,'
                              'any other value to convert binary to decimal: ', int)

if covert_to_binary:
    binary_pattern = r'^[01]+$'
    while True:
        binary_string = input('Enter binary string: ')
        if not re.match(binary_pattern, binary_string):
            print('binary string can only contain 1s and 0s, try again')
            continue
        print(f'{binary_string} in decimal is {to_decimal(binary_string)}')
        break
else:
    decimal_number = get_number('Enter decimal number: ', int)
    print(f'{decimal_number} in binary is {to_binary(decimal_number)}')
