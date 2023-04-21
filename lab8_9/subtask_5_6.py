from utils import get_reg_ex_input


def is_leap_year(month_year: int) -> bool:
    return month_year % 4 == 0 and (month_year % 100 != 0 or month_year % 400 == 0)


def get_days_or_default(month_name: str, month_year: int) -> int:
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

    return None if month_name not in month_days else month_days[month_name]


if __name__ == '__main__':
    # name of the month followed by a space followed by a year from 1900 to 3000 inclusive
    input_pattern = r'^[A-Za-z]+\s(19\d\d|20\d\d|2[4-9]\d\d|3000)$'

    while True:
        message = 'Enter month name and year(1900-3000) separated with a space: '
        user_input = get_reg_ex_input(message, input_pattern)

        month, year = user_input.split(' ')
        year = int(year)
        days = get_days_or_default(month.lower(), year)

        if days is None:
            print(f'month named "{month}" does not exist, try again')
            continue

        leap_year_info = '(leap year)' if is_leap_year(year) else ''

        print(f'{month} {year}{leap_year_info} has {days} days')
        break
