# Multi-paradigm programming languages Lab_5.3 Illia Pasichnichenko IKM-221a
print('Multi-paradigm programming languages Lab 5.3')
print('Illia Pasichnichenko IKM-221a')

eps = 0.0001
x = 1
n = 16

while True:
    x_n = 0.5 * (x + n / x)
    if abs(x - x_n) < eps * x_n:
        break
    x = x_n

print(round(x, 4))
