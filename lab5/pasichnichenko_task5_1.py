from math import factorial
from itertools import takewhile, count

# Multi-paradigm programming languages Lab_5.1 Illia Pasichnichenko IKM-221a
print('Multi-paradigm programming languages Lab 5.1')
print('Illia Pasichnichenko IKM-221a')

N = 1
row = (10 ** -n * factorial(n - 1) for n in count(N))
row_sum = sum(list(takewhile(lambda x: x >= 1e-4, row)))

print(row_sum)
