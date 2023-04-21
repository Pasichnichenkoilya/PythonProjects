import re
from utils import get_reg_ex_input


def to_binary(decimal_value: int) -> str:
    binary = ''
    while decimal_value:
        binary += str(decimal_value % 2)
        decimal_value //= 2
    return binary[::-1]


def to_decimal(binary_value: str) -> float:
    if not re.match(r'^[01]+$', binary_value):
        return None

    decimal = 0
    for digit in binary_value:
        decimal = decimal * 2 + int(digit)
    return decimal


if __name__ == '__main__':
    while True:
        MESSAGE = 'Enter decimal/binary value (add "b" at the end to indicate binary): '
        # includes only numbers and optional 'b' symbol at the end
        NUMBERS_PATTERN = r'^\d+[b]?$'

        user_input = get_reg_ex_input(MESSAGE, NUMBERS_PATTERN)
        from_binary = user_input[-1].lower() == 'b'

        if from_binary and not re.match(r'^[01]+$', user_input[:-1]):
            print('binary string can only contain 1s and 0s')
            continue

        converted_value = to_decimal(user_input[:-1]) if from_binary else to_binary(int(user_input))
        print(f'{user_input} in {"decimal" if from_binary else "binary"} is {converted_value}')
