# 3
file_name = 'learning_python.txt'
lines = []
with open(file_name, 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())
        lines.append(line.strip())

print(lines)

# 4
formatted_lines = [line.replace('Python', 'C') for line in lines]
print('Formatted lines: ')
for line in formatted_lines:
    print(line)
