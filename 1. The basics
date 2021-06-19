# Task_1
# Write a simple function that calculates day of the week for given day of the month and given day of the week for the first day of the month.
# For example, if given day of the month is 7 and day of the week for the first day of the month is 3 (Wednesday) than function should return 2 (which means Tuesday).
# Function signature: def get_day_week (day, starting_dotw)

# Task_2
# Write a simple function which will count number of digits of an natural (integer positive) number.
# Function signature: def count_digits(n)
# Hint: len(str(n)) is wrong, these are features from next chapters, use functions from math 'module'

import math

def get_day_week(day, starting_dotw):
    print((day + starting_dotw - 2) % 7 + 1)

a = int(input())
b = int(input())
get_day_week(a, b)


def count_digits(n):
    return math.floor(math.log(n, 10) + 1)

n = 3714
print("Number of digits : % d" % (count_digits(n)))
