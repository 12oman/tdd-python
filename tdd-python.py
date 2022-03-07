# a test to demonstrate the use of assert

# import the unittest module
import unittest

# import the function to be tested
# from boxProblem import bigBoxes
from boxCalculator import bigBoxes
from boxCalculator import mediumBoxes
from boxCalculator import smallBoxes


# first we create a class that inherits from unittest.
# (this is specific to unittest:)
# this one is called boxTest, but it can be anything
# usually, it is also the same as the name of the file and
# it will be descriptive of what the test is testing and is
# also equal to the Unit under test
class boxProblem(unittest.TestCase):
    # then, we define some test methods.
    # each method is a "test case"
    # the return value of the method is the result of the test
    # which we can call an assertion. It will return True or False
    # our box calculator is supposed to return the number of boxes of each size needed for a given number of items
    # we will therefore test our function with a few different inputs
    # let's define a test method for the number of big boxes
    def test_bigBoxes(self):
        # remember that big boxes hold 5 items
        # so the input 4 should return 0 big boxes, but 5 should return 1
        # we can use the assertEqual method to test the result of the function is equal to this expectation.
        # the expected value is the first parameter, the actual value is the second parameter
        # Arrange, Act Assert is the standard naming convention for test methods
        # in arrange we arrange the input, in act we do the action, and in assert we assert the result
        # arrange
        expected = 0
        # act
        actual = bigBoxes(4)
        # assert
        self.assertEqual(actual, expected)
        # arrange
        expected = 1
        # act
        actual = bigBoxes(5)
        # assert
        self.assertEqual(actual, expected)

    def test_mediumBoxes(self):
        # remember that medium boxes hold 3 items
        # so the input 4 should return 1 medium boxes, but 2 should return 0
        # we can use the assertEqual method to test the result of the function is equal to this expectation.
        # the expected value is the first parameter, the actual value is the second parameter
        # Arrange, Act Assert is the standard naming convention for test methods
        # in arrange we arrange the input, in act we do the action, and in assert we assert the result
        # arrange
        expected = 1
        # act
        actual = mediumBoxes(4)
        # assert
        self.assertEqual(actual, expected)
        # arrange
        expected = 0
        # act
        actual = mediumBoxes(2)
        # assert
        self.assertEqual(actual, expected)

    def test_smallBoxes(self):
        # remember that small boxes hold 1 item each so should be used only
        # in the case that the number of items is not divisible by 5 nor 3
        # so the input 4 should return 1 small boxes, but 5 should return 0
        # we can use the assertEqual method to test the result of the function is equal to this expectation.
        # the expected value is the first parameter, the actual value is the second parameter
        # Arrange, Act Assert is the standard naming convention for test methods
        # in arrange we arrange the input, in act we do the action, and in assert we assert the result
        # arrange
        expected = 1
        # act
        actual = smallBoxes(4)
        # assert
        self.assertEqual(actual, expected)
        # arrange
        expected = 0
        # act
        actual = smallBoxes(5)
        # assert
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    # run the tests
    unittest.main()
    # if we run this file directly, we will run the tests
    # if we import this file as a module it will not run the tests
