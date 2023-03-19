from utils import get_number

parity_info_file_name = 'prime_info.txt'
number = get_number('an integer', int)
parity_info = f'the number {number} is ' + ('odd' if number % 2 else 'even')

print(parity_info)
with open(parity_info_file_name, 'a') as file:
    file.write(f'{parity_info}\n')
