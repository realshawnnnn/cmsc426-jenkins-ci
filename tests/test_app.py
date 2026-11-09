
import unittest

from app import add_numbers, subtract_numbers, multiply_numbers


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtract_numbers(10, 4), 6)

    def test_multiplication(self):
        self.assertEqual(multiply_numbers(3, 5), 15)


if __name__ == "__main__":
    unittest.main()
