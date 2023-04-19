from utils import get_number, get_reg_ex_input


class BasicMathOperations:

    @staticmethod
    def add(left_operand, right_operand):
        return left_operand + right_operand

    @staticmethod
    def diff(left_operand, right_operand):
        return left_operand - right_operand

    @staticmethod
    def divide(left_operand, right_operand):
        return left_operand / right_operand

    @staticmethod
    def multiply(left_operand, right_operand):
        return left_operand * right_operand

    @staticmethod
    def mod(left_operand, right_operand):
        return left_operand % right_operand

    @staticmethod
    def power(left_operand, right_operand):
        return left_operand ** right_operand

    @staticmethod
    def div(left_operand, right_operand):
        return left_operand // right_operand


operations = {'+': BasicMathOperations.add,
              '-': BasicMathOperations.diff,
              '/': BasicMathOperations.divide,
              '*': BasicMathOperations.multiply,
              'mod': BasicMathOperations.mod,
              'pow': BasicMathOperations.power,
              'div': BasicMathOperations.div}

while True:
    a = get_number('Enter a: ', float)
    operation = input('Enter choose operation [+, -, /, *, mod, pow, div]: ').strip()

    if operation not in operations:
        print(f'operation {operation} not found, try again')
        continue

    not_zero_numbers = r'^[1-9][0-9]*$'
    b = float(get_reg_ex_input('Enter b: ', not_zero_numbers,
                               'invalid input, enter number (not equal to 0)'))

    print(f'{a} {operation} {b} = {operations[operation](a, b)}')
    break
