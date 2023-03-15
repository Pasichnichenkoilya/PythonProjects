from utils import get_number

print('Multi-paradigm programming languages Lab 4')
print('Illia Pasichnichenko IKM-221a')

number = get_number('an integer', int)
result = 0

for i in range(1, number * 2, 2):
    result += i / (i + 1)

print('Result: ', result)
