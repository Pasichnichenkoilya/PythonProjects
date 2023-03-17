from math import factorial

# Multi-paradigm programming languages Lab_5.1 Illia Pasichnichenko IKM-221a
print('Multi-paradigm programming languages Lab 5.1')
print('Illia Pasichnichenko IKM-221a')

epsilon = 10 ** - 4
series_sum = 0
n = 1
a = 1

while abs(a) >= epsilon:
    a = 10 ** -n * factorial(n - 1)
    series_sum += a
    n += 1

print(series_sum)
