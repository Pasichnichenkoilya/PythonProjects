from utils import get_number
from functools import reduce


def add(current_sum, current_number):
    return current_sum + current_number / (current_number + 1)


print('Multi-paradigm programming languages Lab 4')
print('Illia Pasichnichenko IKM-221a')

number = get_number('an integer', int)

odd_numbers = range(1, number * 2, 2)
result = reduce(add, odd_numbers, 0)

print('Result: ', result)
