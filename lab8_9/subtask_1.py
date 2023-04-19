names = ['Sophia', 'Emma', 'Ethan', 'Liam', 'Madison',
         'Admin', 'Olivia', 'William', 'Benjamin', 'Charlotte']
greetings = [f"{name}, I hope you're well" if name == 'Admin' else
             f'{name}, thank you for logging in again..' for name in names]

result_output = '\n'.join(greetings) if greetings else 'We need to find some users!'
print(result_output)
