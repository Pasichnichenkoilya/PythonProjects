file_name = 'The Count of Monte Cristo.txt'

with open(file_name, 'r', encoding='utf-8') as file:
    all_letters = [char for char in file.read() if char.isalpha()]
    upper = [letter for letter in all_letters if letter.isupper()]
    upper_percentage = len(upper) / len(all_letters) * 100

    print(f'upper: {round(upper_percentage)}%, lower: {100 - round(upper_percentage)}%')
