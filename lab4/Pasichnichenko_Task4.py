from utils import get_number
from functools import reduce

print('Multi-paradigm programming languages Lab 4')
print('Illia Pasichnichenko IKM-221a')

number = get_number('an integer', int)


def add(current_sum, current_number):
    return current_sum + current_number / (current_number + 1)


result = reduce(add, range(1, number * 2, 2), 0)

print('Result: ', result)
