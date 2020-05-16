# import calendar info
import calendar

# weekheader first 3 charactors
print(calendar.weekheader(3))
print()

# first weekday
print(calendar.firstweekday())
print()

# calendar month
print(calendar.month(2020, 5,))

#  matrix of calendar
print(calendar.monthcalendar(2020, 5))

# calendar for the entire year
print(calendar.calendar(2020 ))

# what day of the week
day_of_the_week = calendar.weekday(2020, 5, 17)
print(day_of_the_week)
print()

# is 2020 a leap year
is_leap = calendar.isleap(2020)
print(is_leap)
print()

# how many leap days by year
how_many_leap_days  =calendar.leapdays(2000,2005)
print(how_many_leap_days)
