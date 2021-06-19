# Task_1
# Write a simple function which will transform a list of temperature values in Fahrenheit to a list of temperature values in Celsius.
# Use .map() function and lambda expression in this task.
# Function signature: def to_celsius(temperature_list)

# Task_2
# Write a simple program to make a chain of function decorators for html text formatting (bold, italic, underline).
# It should works like this:
# @bold 
# @italic 
# @underline 
# def get_text(): 
#   return "hello world" 

# print(get_text()) # shows "<b><i><u>hello world</u></i></b>"

# Task_3
# 1) For given function (with one parameter, parameter type and return value type are equal) generate another function that applies original fuction multiple times.
# Example:
# from math import sin
# f1 = fn(lambda x: "sin(%s)" % x, 5)
# f2 = fn(lambda x: sin(x), 5)
# print("%s = %f" % (f1("1"), f2(1)))
# >>sin(sin(sin(sin(sin(1))))) = 0.587181
# print("%s = %f" % (f1("2"), f2(2)))
# >>sin(sin(sin(sin(sin(2))))) = 0.606464
# print(fn(lambda x: sin(x), 0)(1000))
# >> 1000
# Function signature: def fn (f, n)

# 2) Using 'fn' (see first part of the task) generate function that calculates golden ratio approximation.
# final formula:
# 1 + 1 / (1 + 1 / (1 + 1 / (...)))

# some results:
# golden_ratio(0) = 1
# golden_ratio(1) = 2
# golden_ratio(2) = 1.5
# golden_ratio(100) = 1.6180...

# Function signature: def golden_ratio (n), where 'n' is number of invocations (and number of terms in continued fraction)

# Task_4
# Write a function that produces stream generator for given iterable object (list, generator, etc) whose elements contain position and value and sorted by order of apperance.
# Stream generator should be equal to initial stream (without position) but gaps filled with zeroes. For example:
# >>> gen = gen_stream(9,[(4,111),(7,12)])
# >>> list(gen) [0, 0, 0, 0, 111, 0, 0, 12, 0] # first element has zero index, so 111 located on fifth position, 12 located on 8th position
# I.e. 2 significant elements has indexes 4 and 7, all other elements filled with zeroes.
# To simplify things elements are sorted (i.e element with lower position should precede element with higher number) in initial stream.

# First parameter can be None, in this case stream should be inifinite, e.g. infinite zeroes stream:
# >>> gen_stream(None, [])
# following stream starts with 0, 0, 0, 0, 111, 0, 0, 12, ... then infinitely generates zeroes:
# >>> gen_stream(None, [(4,111),(7,12)])

# Function should also support custom position-value extractor for more advanced cases, e.g.
# >>>
# def day_extractor(x):
#  months = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
#  acc = sum(months[:x[1]-1]) + x[0] - 1
#  return (acc, x[2])
# >>> precipitation_days = [(3, 1, 4), (5, 2, 6)]
# >>> list(gen_stream(59, precipitation_days, day_extractor)) #59: January and February to limit output
# [0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# precipitation_days format is following: (d, m, mm), where d - day in month, m - month, mm - precipitation in millimeters
# So, in example:
# (3, 1, 4) - January,3 precipitation: 4 mm
# (5, 2, 6) - February,5 precipitation: 6 mm
# Extractor passed as optional third parameter with default value - lambda function that handles (position, value) pairs like in first example.

# Function signature: def gen_stream (total, sorted_iterable, extractor)


# Task_1
def to_celsius(temperature_list):
    return list(map(lambda f: ((5.0 / 9.0) * (f - 32)), temperature_list))


fahrenheit = [51, 102, 110, 115]
print(to_celsius(fahrenheit))


# Task_2
def bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


def underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"

    return wrapped


@bold
@italic
@underline
def get_text():
    return "hello world"


print(get_text())  # shows "<b><i><u>hello world</u></i></b>"

# Task_3
from math import sin


def fn(f, n):
    def wrap(*arg):
        for _ in range(n):
            if isinstance(arg, tuple):
                arg = f(*arg)
            else:
                arg = f(arg)
        return arg

    return wrap


f1 = fn(sin, 5)
f1(1)


def fib(q, w):
    q, w = w, q + w
    return q, w


f2 = fn(fib, 100)


def golden_ratio(n):
    f = fn(lambda x, y: (y, x + y), n + 1)
    q, w = f(0, 1)
    return w / q


print(golden_ratio(0))
print(golden_ratio(1))
print(golden_ratio(2))
print(golden_ratio(100))


# Task_4
def gen_stream(total, sorted_iterable, extractor=lambda x: x):
    elem_iter = iter(map(extractor, sorted_iterable))
    pos, val = next(elem_iter, (None, None))
    cnt = 0
    while total is None or cnt < total:
        if cnt == pos:
            yield val
            pos, val = next(elem_iter, (None, None))
        else:
            yield 0
        cnt += 1


def day_extractor(x):
    months = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
    acc = sum(months[:x[1] - 1]) + x[0] - 1
    return acc, x[2]


precipitation_days = [(3, 1, 4), (5, 2, 6)]
list(gen_stream(59, precipitation_days, day_extractor))




