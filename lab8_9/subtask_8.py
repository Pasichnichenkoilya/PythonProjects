from utils import get_number


def add(left_operand, right_operand):
    return left_operand + right_operand


def diff(left_operand, right_operand):
    return left_operand - right_operand


def divide(left_operand, right_operand):
    return left_operand / right_operand


def multiply(left_operand, right_operand):
    return left_operand * right_operand


def mod(left_operand, right_operand):
    return left_operand % right_operand


def power(left_operand, right_operand):
    return left_operand ** right_operand


def div(left_operand, right_operand):
    return left_operand // right_operand


operations = {'+': add,
              '-': diff,
              '/': divide,
              '*': multiply,
              'mod': mod,
              'pow': power,
              'div': div}

while True:
    a = get_number('Enter a: ', float)
    operation = input('Enter choose operation [+, -, /, *, mod, pow, div]: ').strip()

    if operation not in operations:
        print(f'operation {operation} not found, try again')
        continue

    b = get_number('Enter b: ', float)
    if operation == '/' or operation == 'div' and b == 0:
        print('cannot divide by zero')
        continue

    print(f'{a} {operation} {b} = {operations[operation](a, b)}')
    break
