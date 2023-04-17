import re

letters_parity = {letter: i % 2 for i, letter in enumerate('abcdefgh')}
coord_pattern = '^[a-h][1-8]$'

while True:
    user_input = input('Enter square coordinate, example - a1, b6, h8: ').strip()

    if not re.match(coord_pattern, user_input):
        print(f'Coordinate {user_input} does not exist')
        continue

    letter = user_input[0]
    number = int(user_input[1])

    is_white = letters_parity[letter] if number % 2 else not letters_parity[letter]
    print(f'{user_input} square is {"white" if is_white else "black"}')
