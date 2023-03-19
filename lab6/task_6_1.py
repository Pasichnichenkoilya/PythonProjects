file_name = 'numbers.txt'
save_sum_file_name = 'sum_numbers.txt'
with open(file_name, 'r') as file:
    numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
    sum_numbers = sum(numbers)
    print(sum_numbers)
    with open(save_sum_file_name, 'w') as save_file:
        save_file.write(f'{sum_numbers}\n')
