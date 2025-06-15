# File: test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5.0)
        self.assertEqual(self.calc.add(-1, 5), 4.0)
        self.assertEqual(self.calc.add(0, 0), 0.0)
        self.assertEqual(self.calc.add(-3, -7), -10.0)
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5.0)
        self.assertEqual(self.calc.subtract(-3, 3), -6.0)
        self.assertEqual(self.calc.subtract(0, 0), 0.0)
        self.assertEqual(self.calc.subtract(5, 10), -5.0)
        self.assertAlmostEqual(self.calc.subtract(3.5, 1.2), 2.3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20.0)
        self.assertEqual(self.calc.multiply(-2, 3), -6.0)
        self.assertEqual(self.calc.multiply(0, 100), 0.0)
        self.assertEqual(self.calc.multiply(-4, -5), 20.0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertEqual(self.calc.divide(0, 10), 0.0)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

if __name__ == '__main__':
    unittest.main()
