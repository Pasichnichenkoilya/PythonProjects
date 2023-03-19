file_name = 'The Life and Adventures of Robinson Crusoe By Daniel Defoe.txt'
formatted_text_file_name = 'formatted_text.txt'

with open(file_name, 'r', encoding='utf-8') as file:
    text = file.read()
    formatted_text = text.replace('\n', ' ')
    with open(formatted_text_file_name, 'w', encoding='utf-8') as formatted_file:
        formatted_file.write(formatted_text)

print('Formatting complete')
