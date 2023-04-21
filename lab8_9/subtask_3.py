def get_number_names(numbers: list[int]) -> list[str]:
    str_numbers = []
    for i in numbers:
        if i == 1:
            str_numbers.append(f'{1}st')
        elif i == 2:
            str_numbers.append(f'{i}nd')
        elif i == 3:
            str_numbers.append(f'{i}rd')
        else:
            str_numbers.append(f'{i}th')
    return str_numbers


if __name__ == '__main__':
    one_to_nine = list(range(1, 10))
    print('\n'.join(get_number_names(one_to_nine)))
