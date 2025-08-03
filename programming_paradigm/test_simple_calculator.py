import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(10, -4), 6)


    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(7,0), 7)
        self.assertEqual(self.calc.subtract(0, 5), -5)



    def test_multiply(self):
        self.assertEqual(self.calc.multiply(7, 7), 49)
        self.assertEqual(self.calc.multiply(-4, -3), 12)




    def test_divide(self):
        self.assertEqual(self.calc.divide(25, 5), 5)
        result = self.calc.divide(10,0)
        self.assertIsNone(result)
        result = self.calc.divide(-10,0)
        self.assertIsNone(result)
        result = self.calc.divide(0,0)
        self.assertIsNone(result)
        result = self.calc.divide(0, 5)
        self.assertEqual(result, 0)
        result = self.calc.divide(0, -3)
        self.assertEqual(result, 0)
        result = self.calc.divide(-12, -3)
        self.assertEqual(result, 4)
        result = self.calc.divide(-15, 3)
        self.assertEqual(result, -5)
        result = self.calc.divide(20, -4)
        self.assertEqual(result, -5)



if __name__ == "__main__":
    unittest.main()