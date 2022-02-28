# a tdd refactor of boxProblem 

# import math
from math import floor

# define bigBoxes function
def bigBoxes(items):
    big = floor(items // 5)
    return big
def mediumBoxes(items):
    medium = floor(items % 5 / 3)
    return medium
def smallBoxes(items):
    small = (items % 5) % 3
    return small
def totalBoxes(items):
    total = bigBoxes(items) + mediumBoxes(items) + smallBoxes(items)
    return total
def main():
    items = int(input("Please enter the number of items: "))
    print(items)
    print("total Boxes used: ", totalBoxes(items))
    print("Number of big boxes used: ", bigBoxes(items))
    print("Number of medium boxes used: ", mediumBoxes(items))
    print("Number of small boxes used: ", smallBoxes(items))
# main()