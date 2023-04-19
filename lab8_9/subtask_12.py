import re
import random
from utils import get_number

OPTIONS = ['🪨', '📃', '✂️']


def check_winner(user_option, computer_option):
    if user_option == computer_option:
        print('Draw!')
        return None

    outcomes = {('🪨', '✂️'): 'You Win!',
                ('✂️', '📃'): 'You Win!',
                ('📃', '🪨'): 'You Win!',
                ('✂️', '🪨'): 'I Win!',
                ('📃', '✂️'): 'I Win!',
                ('🪨', '📃'): 'I Win!'}

    print(outcomes[(user_option, computer_option)])


while True:
    print('Choose wisely, username:')
    options_str = ''.join([f'{i + 1} - {option}\n' for i, option in enumerate(OPTIONS)])
    option = get_number(options_str, int)

    # accept only 1, 2, 3 numbers
    if not re.match(r'^[123]$', str(option)):
        print('only numbers from 1 to 3 are acceptable')
        continue
    random_option = random.choice(OPTIONS)
    print(f'You chose {OPTIONS[option - 1]}, I chose {random_option}')
    check_winner(OPTIONS[option - 1], random_option)
