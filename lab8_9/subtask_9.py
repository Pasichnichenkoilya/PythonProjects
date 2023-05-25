from utils import get_number

BANKNOTES = {1: 'Vladimir the Great',
             2: 'Yaroslav the Wise',
             5: 'Bohdan Khmelnytsky',
             10: 'Ivan Mazepa',
             20: 'Ivan Franko',
             50: 'Mikhail Grushevsky',
             100: 'Taras Shevchenko',
             200: 'Lesya Ukrainka',
             500: 'Grigory Skovoroda',
             1000: 'Vladimir Vernadsky'}


def get_banknote_person(banknote_value: int) -> str:
    return BANKNOTES.get(banknote_value, None)


if __name__ == '__main__':
    while True:
        number = get_number('Enter banknote value: ', int)
        name = get_banknote_person(number)
        if name is None:
            print(f'Banknote with value {number} does not exist')
            continue
        print(name)
        break
