import unittest
from numeric_functions import add, subtract, multiply, divide

class testNumericFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(5,5), 10)
        self.assertEqual(add(5,10), 15)
        self.assertEqual(add(5,-10), -5)

    def test_subtraction(self):
        self.assertEqual(subtract(5,5), 0)
        self.assertEqual(subtract(5,10), -5)
        self.assertEqual(subtract(5,-10), 15)

    def test_mutliplication(self):
        self.assertEqual(multiply(5,5), 25)
        self.assertEqual(multiply(5,10), 50)
        self.assertEqual(multiply(5,-10), -50)

    def test_division(self):
        self.assertEqual(divide(5,5), 1)
        self.assertEqual(divide(5,10), .5)
        self.assertEqual(divide(5,-10), -.5)
        self.assertRaises(ZeroDivisionError, divide, 5, 0)

if __name__ == '__main__':
    unittest.main()