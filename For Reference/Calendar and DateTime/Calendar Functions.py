import calendar

our_date = input('Please enter the date in Date-Month-Year format: ')

separators_dict = {' ':'/','-':'/','.':'/'}

for key, value in separators_dict.items():
    our_date = our_date.replace(key, value)
d, m, y = map(int, our_date.split(sep='/'))

weekday_num = calendar.weekday(y, m, d)
print(f'Weekday number is {weekday_num}')

our_day = calendar.day_name[weekday_num]
print(f'It is {our_day} on {our_date}')
