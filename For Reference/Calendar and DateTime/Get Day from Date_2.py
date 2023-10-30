import calendar

# input('Enter the date below in MM DD YYYY format:\n')

month, day, year = map(int, input().split())

print(calendar.day_name[calendar.weekday(year, month, day)].upper())
