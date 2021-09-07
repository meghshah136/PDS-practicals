'''Ram wants to know age of his grandfather who was born on 18th December,1950.
   Kindly help ram to know how old is his grandfather? Also, print the calendar
   for the month and year on which ram’s grandfather was born. '''

import calendar
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - (int((today.month, today.day) < (birth_date.month, birth_date.day)))
    return age

d = int(input("Enter Day   : "))
m = int(input("Enter Month : "))
y = int(input("Enter Year  : "))
print(calculate_age(date(y, m, d)), "years")
print(calendar.month(y, m))
print(calendar.calendar(y))