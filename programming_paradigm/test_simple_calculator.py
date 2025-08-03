import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add_positive_number(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_add_negative_number(self):
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_add_positive_and_negative(self):
        self.assertEqual(self.calc.add(10, -4), 6)

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)


    def test_subtract_with_zero(self):
        self.assertEqual(self.calc.subtract(7,0), 7)
        self.assertEqual(self.calc.subtract(0, 5), -5)


    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(7, 7), 49)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -3), 12)


    def test_divide_positive_number(self):
        self.assertEqual(self.calc.divide(25, 5), 5)

    def test_divide_by_zero(self):
        result = self.calc.divide(10,0)
        self.assertIsNone(result)
        result = self.calc.divide(-10,0)
        self.assertIsNone(result)
        result = self.calc.divide(0,0)
        self.assertIsNone(result)

    def test_divide_zero_by_number(self):
        result = self.calc.divide(0, 5)
        self.assertEqual(result, 0)
        result = self.calc.divide(0, -3)
        self.assertEqual(result, 0)

    def test_divide_negative_numbers(self):
        result = self.calc.divide(-12, -3)
        self.assertEqual(result, 4)
        result = self.calc.divide(-15, 3)
        self.assertEqual(result, -5)
        result = self.calc.divide(20, -4)
        self.assertEqual(result, -5)