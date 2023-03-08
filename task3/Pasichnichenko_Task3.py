from math import sin, atan

# Multi-paradigm programming languages Lab2 Illia Pasichnichenko IKM-221a
print('Multi-paradigm programming languages Lab2')
print('Illia Pasichnichenko IKM-221a')

a = float(input("Enter a value: "))
while a == 0:
    a = float(input('a cannot be equal to 0, enter valid number'))

b = float(input("Enter b value: "))
while b == 0:
    b = float(input('b cannot be equal to 0, enter valid number'))

c = float(input("Enter c value: "))

y = (sin(2 * a) / a - 3) + (atan(b) / c)

print(y)
