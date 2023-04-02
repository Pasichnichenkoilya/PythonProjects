from utils import get_number

number = 1
numbers_sum = 0
while number:
    number = get_number('Enter an integer(0 to exit): ', int)
    numbers_sum += number

print(f'sum = {numbers_sum}')
