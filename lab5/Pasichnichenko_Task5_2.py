from utils import get_number

# Multi-paradigm programming languages Lab_5.2 Illia Pasichnichenko IKM-221a
print('Multi-paradigm programming languages Lab 5.2')
print('Illia Pasichnichenko IKM-221a')

number = get_number('an integer', int)
digits = 0

while number > 0:
    number //= 10
    digits += 1

print(f'The number has {digits} digits')
