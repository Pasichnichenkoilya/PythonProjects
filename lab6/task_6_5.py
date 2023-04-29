file_name = 'guest_book.txt'
stop_symbol = r'\0'
with open(file_name, 'a', encoding='utf-8') as file:
    while True:
        name = input(f'Enter guest name, to exit enter {stop_symbol}: ')
        if name == stop_symbol:
            break
        print(f'Hello, {name}')
        file.write(f'{name}\n')
