file_name = 'numbers.txt'
save_sum_file_name = 'sum_numbers.txt'

with open(file_name, 'r', encoding='utf-8') as file:
    sum_numbers = sum(int(line.strip()) for line in file if line.strip().isdigit())
    print(sum_numbers)

with open(save_sum_file_name, 'w', encoding='utf-8') as save_file:
    save_file.write(f'{sum_numbers}\n')
