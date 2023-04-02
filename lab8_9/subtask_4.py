from utils import get_number

number = get_number('Enter an integer: ', int)
parity = 'odd' if number % 2 else 'even'

print(f'The number is {parity}')
