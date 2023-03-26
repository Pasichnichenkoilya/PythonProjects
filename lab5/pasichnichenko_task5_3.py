# Multi-paradigm programming languages Lab_5.3 Illia Pasichnichenko IKM-221a
print('Multi-paradigm programming languages Lab 5.3')
print('Illia Pasichnichenko IKM-221a')

EPS = 0.0001
N = 16
x = 1

while True:
    x_n = 0.5 * (x + N / x)
    if abs(x - x_n) < EPS * x_n:
        break
    x = x_n

print(round(x, 4))
