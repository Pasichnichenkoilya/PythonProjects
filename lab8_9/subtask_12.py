import re
import random
from utils import get_number

options = ['🪨', '📃', '✂️']


def check_winner(user_option, computer_option):
    if user_option == computer_option:
        print('Draw!')
    elif user_option == '🪨' and computer_option == '✂️' or \
            user_option == '📃' and computer_option == '🪨' or \
            user_option == '✂️' and computer_option == '📃':
        print('You Win!')
    else:
        print('I Win!')


while True:
    print('Choose wisely, username:')
    options_str = ''.join([f'{i + 1} - {option}\n' for i, option in enumerate(options)])
    option = get_number(options_str, int)

    # accept only 1, 2, 3 numbers
    if not re.match(r'^[123]$', str(option)):
        print('only numbers from 1 to 3 are acceptable')
        continue
    random_option = random.choice(options)
    print(f'You chose {options[option - 1]}, I chose {random_option}')
    check_winner(options[option - 1], random_option)
