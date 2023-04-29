file_name = 'The Life and Adventures of Robinson Crusoe By Daniel Defoe.txt'

with open(file_name, 'r', encoding='utf-8') as file:
    text = file.read().lower()
    print(text.count('the'))
