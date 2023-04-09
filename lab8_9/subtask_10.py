from utils import get_number

letters = 'abcdefgh'
letters_parity = {letter: i % 2 for i, letter in enumerate(letters)}

while True:
    letter = input('Enter letter[a-h]: ').strip()[0]
    number = get_number('Enter number[1-8]: ', int)

    if letter not in letters or number < 1 or number > 8:
        print(f'Coordinate {letter}{number} does not exist')
        continue

    square_color = 'black' if not letters_parity[letter] % 2 else 'white'
    print(f'{letter}{number} square is {square_color}')
