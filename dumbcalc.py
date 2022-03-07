# a function which adds any number of numbers
def add(*args):
    return sum(args)

# subtract a list of numbers from the first number


# def subtract(*args):
#     return args[0] - sum(args[1:])


# def multiply(*args):
#     return args[0] * sum(args[1:])

# arrange
expected = 10
# act
actual = add(1, 2, 3, 4)
# does the add function return the expected value?
testcase_assertion = f'expected: {expected}, actual: {actual}, test pass: {actual == expected}'
# assert
print(testcase_assertion)
# print(multiply(2, 3, 5))
