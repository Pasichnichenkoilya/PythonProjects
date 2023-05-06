from utils import get_number


def get_parity(number: int) -> str:
    return 'The number is ' + ('odd' if number % 2 else 'even')


if __name__ == '__main__':
    input_number = get_number('Enter an integer: ', int)
    print(get_parity(input_number))
