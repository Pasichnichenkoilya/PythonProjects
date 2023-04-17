from utils import get_number

banknotes = {1: 'Vladimir the Great',
             2: 'Yaroslav the Wise',
             5: 'Bohdan Khmelnytsky',
             10: 'Ivan Mazepa',
             20: 'Ivan Franko',
             50: 'Mikhail Grushevsky',
             100: 'Taras Shevchenko',
             200: 'Lesya Ukrainka',
             500: 'Grigory Skovoroda',
             1000: 'Vladimir Vernadsky'}

while True:
    number = get_number('Enter banknote value: ', int)

    if number not in banknotes:
        print(f'Banknote with value {number} does not exist')
        continue
    print(banknotes[number])
    break
