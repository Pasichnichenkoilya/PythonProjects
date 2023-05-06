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
        if right_operand == 0:
            return None
        return left_operand % right_operand

    @staticmethod
    def power(left_operand, right_operand):
        return left_operand ** right_operand

    @staticmethod
    def div(left_operand, right_operand):
        if right_operand == 0:
            return None
        return left_operand // right_operand


def get_valid_number(operation):
    if operation in ('/', 'div', 'mod'):
        not_zero_numbers = r'^-?(?!0+$)\d+(?:\.\d+)?$'
        return float(get_reg_ex_input('Enter b: ', not_zero_numbers,
                                      'cannot divide by zero, enter valid number:'))
    return get_number('Enter b: ', float)


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
        input_operation = input('Enter operation [+, -, /, *, mod, pow, div]: ').strip()

        if input_operation not in operations:
            print(f'operation {input_operation} not found, try again')
            continue

        b = get_valid_number(input_operation)

        print(f'{a} {input_operation} {b} = {operations[input_operation](a, b)}')
        break
