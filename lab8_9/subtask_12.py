import random
from utils import get_reg_ex_input


def check_winner(user_option, computer_option):
    outcomes = {('🪨', '🪨'): 'Draw!',
                ('✂️', '✂️'): 'Draw!',
                ('📃', '📃'): 'Draw!',
                ('🪨', '✂️'): 'You Win!',
                ('✂️', '📃'): 'You Win!',
                ('📃', '🪨'): 'You Win!',
                ('✂️', '🪨'): 'I Win!',
                ('📃', '✂️'): 'I Win!',
                ('🪨', '📃'): 'I Win!'}

    if (user_option, computer_option) not in outcomes:
        return None

    return outcomes[(user_option, computer_option)]


if __name__ == '__main__':
    OPTIONS = ['🪨', '📃', '✂️']

    while True:
        print('Choose wisely, username:')

        options_str = ''.join([f'{i + 1} - {option}\n' for i, option in enumerate(OPTIONS)])
        option = int(get_reg_ex_input(options_str, r'^[123]$'))

        random_option = random.choice(OPTIONS)
        print(f'You chose {OPTIONS[option - 1]}, I chose {random_option}')
        print(check_winner(OPTIONS[option - 1], random_option))
