# let's make a unit test for dumbcalc

import unittest

from dumbcalc import add, multiply, subtract


# definte a unittest


class calculatorTest(unittest.TestCase):
    # define some test cases
    def test_add_2_numbers(self):
        # arrange
        expected = 3
        # act
        actual = add(1, 2)
        # does the add function return the expected value?
        print(
            f'expected: {expected}, actual: {actual}, test pass: {actual == expected}')

        # act
        # assert
        self.assertEqual(actual, expected)

    def test_add_4_numbers(self):
        # arrange
        expected = 10
        # act
        actual = add(1, 2, 3, 4)
        # does the add function return the expected value?
        print(
            f'expected: {expected}, actual: {actual}, test pass: {actual == expected}')

        # act
        # assert
        self.assertEqual(actual, expected)

    def test_subtract_2_numbers(self):
        expected = 7
        actual = subtract(10, 3)
        print(
            f'expected: {expected}, actual: {actual}, test pass: {actual == expected}')
        self.assertEqual(actual, expected)

    def test_subtract_4_numbers(self):
        expected = 1
        actual = subtract(10, 3, 2, 1, 3)
        print(
            f'expected: {expected}, actual: {actual}, test pass: {actual == expected}')
        self.assertEqual(actual, expected)

    def test_multiply_2_numbers(self):
        expected = 50
        actual = multiply(10, 5)
        print(
            f'expected: {expected}, actual: {actual}, test pass: {actual == expected}')
        self.assertEqual(actual, expected)

    def test_multiply_3_numbers(self):
        expected = 162
        actual = multiply(9, 6, 3)
        print(
            f'expected: {expected}, actual: {actual}, test pass: {actual == expected}')
        self.assertEqual(actual, expected)

    def test_multiply_8_numbers(self):
        expected = 362880
        actual = multiply(9, 8, 7, 6, 5, 4, 3, 2)
        print(
            f'expected: {expected}, actual: {actual}, test pass: {actual == expected}')
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
