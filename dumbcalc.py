# a function which adds any number of numbers
from functools import reduce


def add(*args):
    return sum(args)

# subtract a list of numbers from the first number

# overdeterming the function
# def subtract(a, b):
#     return a - b


def subtract(*args):
    return args[0] - sum(args[1:])

# multiply any number of numbers


# def multiply(*args):
#     return args[0] * multiply(args[1:])

def multiply(*args):
    return reduce(lambda x, y: x * y, args)


# arrange
# print(multiply(2, 3, 5))
