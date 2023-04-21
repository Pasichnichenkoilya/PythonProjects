from utils import get_reg_ex_input


def get_square_color(square_letter: str, square_number: int) -> str:
    letters_parity = {l: i % 2 for i, l in enumerate('abcdefgh')}

    if square_letter not in letters_parity or (square_number < 1 or square_number > 8):
        return None

    is_white = letters_parity[square_letter] \
        if square_number % 2 \
        else not letters_parity[square_letter]

    return 'white' if is_white else 'black'


if __name__ == '__main__':
    coord_pattern = '^[a-h][1-8]$'
    while True:
        user_input = get_reg_ex_input('Enter square coordinate, example - a1, b6, h8: ',
                                      coord_pattern,
                                      'Coordinate does not exist')
        input_letter = user_input[0]
        input_number = int(user_input[1])
        color = get_square_color(input_letter, input_number)

        print(f'{user_input} square is {color}')
