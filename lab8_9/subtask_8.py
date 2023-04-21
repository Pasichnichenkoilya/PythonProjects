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
        if right_operand == 0:
            return None
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
        if right_operand == 0:
            return None
        return left_operand // right_operand


if __name__ == '__main__':
    operations = {'+': BasicMathOperations.add,
                  '-': BasicMathOperations.diff,
                  '/': BasicMathOperations.divide,
                  '*': BasicMathOperations.multiply,
                  'mod': BasicMathOperations.mod,
                  'pow': BasicMathOperations.power,
                  'div': BasicMathOperations.div}

    while True:
        a = get_number('Enter a: ', float)
        operation = input('Enter operation [+, -, /, *, mod, pow, div]: ').strip()

        if operation not in operations:
            print(f'operation {operation} not found, try again')
            continue

        if operation in ('/', 'div'):
            not_zero_numbers = r'^-?(?!0+$)\d+(?:\.\d+)?$'
            b = float(get_reg_ex_input('Enter b: ', not_zero_numbers,
                                       'cannot divide by zero, enter valid number:'))
        else:
            b = get_number('Enter b: ', float)

        print(f'{a} {operation} {b} = {operations[operation](a, b)}')
        break
