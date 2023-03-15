from utils import get_int

print('Multi-paradigm programming languages Lab 4')
print('Illia Pasichnichenko IKM-221a')

number = get_int('an integer')
result = 0

for i in range(1, number * 2, 2):
    result += i / (i + 1)

print('Result: ', result)
