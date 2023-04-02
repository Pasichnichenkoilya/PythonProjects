from re import match

regex_pattern = r'^CHAPTER [IVXLCDM]+\..*\n$'
file_name = 'The Life and Adventures of Robinson Crusoe By Daniel Defoe.txt'
chapters_file_name = 'chapters.txt'

with open(file_name, mode='r', encoding='utf-8') as file:
    chapters = [line for line in file if match(regex_pattern, line)]

with open(chapters_file_name, 'w', encoding='utf-8') as chapters_file:
    chapters_file.writelines(chapters)

print(f'Chapter names saved to {chapters_file_name}')
