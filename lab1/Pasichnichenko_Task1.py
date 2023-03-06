# 3.1
cource_task_name = 'Multi-paradigm programming languages', 'Task 1'
print(':'.join(cource_task_name))

student_info = {'name': 'Illia', 'surname': 'Pasichnichenko', 'group': 'IKM-221a'}
print(' '.join(student_info.values()))

# 3.2
for i in range(45):
    separator = ', ' if i < 44 else '\n'
    print('Vladyslav Valeriyovych Ovsyannikov', end=separator)

# 3.2
result = (11 + 2 * 3 + 4.1) / (12.4 - 221.3) + 4.8
print(result)
