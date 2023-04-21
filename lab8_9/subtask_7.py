from utils import get_number


def get_numbers_sum(numbers: list[int]) -> int:
    return sum(numbers)


if __name__ == '__main__':
    input_numbers = []

    while True:
        number = get_number('Enter an integer(0 to exit): ', int)
        if number == 0:
            break
        input_numbers.append(number)

    print(get_numbers_sum(input_numbers))
