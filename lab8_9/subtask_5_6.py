import re


def is_leap_year(month_year: int):
    return month_year % 4 == 0 and (month_year % 100 != 0 or month_year % 400 == 0)


def get_days(month_name: str, month_year: int):
    month_days = {
        'january': 31,
        'february': 29 if is_leap_year(month_year) else 28,
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31
    }
    return month_days[month_name]


# name of the month followed by a space followed by a year from 1900 to 3000 inclusive
input_pattern = r'^[A-Za-z]+\s(19\d\d|20\d\d|2[4-9]\d\d|3000)$'

months = ['january', 'february', 'march', 'april', 'may', 'june',
          'july', 'august', 'september', 'october', 'november', 'december']

while True:
    user_input = input('Enter month name and year(1900-3000) separated with a space: ')

    if not re.match(input_pattern, user_input):
        print('invalid input, try again')
        continue

    month, year = user_input.split(' ')
    if month.lower() not in months:
        print(f'month named "{month}" does not exist, try again')
        continue

    year = int(year)
    days = get_days(month, year)
    leap_year_info = '(leap year)' if is_leap_year(year) else ''

    print(f'{month} {year}{leap_year_info} has {days} days')
    break
