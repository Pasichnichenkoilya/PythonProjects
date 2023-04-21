def get_greetings(user_names):
    greetings = [f"{name}, I hope you're well" if name == 'Admin' else
                 f'{name}, thank you for logging in again..' for name in user_names]

    return greetings if greetings else ['We need to find some users!']


if __name__ == '__main__':
    names = ['Sophia', 'Emma', 'Ethan', 'Liam', 'Madison',
             'Admin', 'Olivia', 'William', 'Benjamin', 'Charlotte']
    print('\n'.join(get_greetings(names)))
