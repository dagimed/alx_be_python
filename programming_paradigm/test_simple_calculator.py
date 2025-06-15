import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various inputs."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        
        # Test with zero
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, -3), -3)
        
        # Test decimal numbers
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertAlmostEqual(self.calc.add(-1.5, 2.5), 1.0)

    def test_subtraction(self):
        """Test the subtraction method with various inputs."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 7), 3)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-3, -5), 2)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        
        # Test decimal numbers
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.3), 3.2)
        self.assertAlmostEqual(self.calc.subtract(-2.5, 1.5), -4.0)

    def test_multiplication(self):
        """Test the multiplication method with various inputs."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 6), 42)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(3, -4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, -3), 0)
        
        # Test with one
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(1, -7), -7)
        
        # Test decimal numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calc.multiply(-1.5, 2.0), -3.0)

    def test_division(self):
        """Test the division method with various inputs."""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        
        # Test decimal numbers
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(-6.6, 3.3), -2.0)
        
        # Test division resulting in fractions
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333)
        self.assertAlmostEqual(self.calc.divide(2, 3), 0.6666666666666666)
        
        # Test dividing by one
        self.assertEqual(self.calc.divide(5, 1), 5.0)
        self.assertEqual(self.calc.divide(-7, 1), -7.0)
        
        # Test dividing zero by a number
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(3.14, 0))

    def test_large_numbers(self):
        """Test operations with large numbers."""
        large_num1 = 1000000
        large_num2 = 999999
        
        self.assertEqual(self.calc.add(large_num1, large_num2), 1999999)
        self.assertEqual(self.calc.subtract(large_num1, large_num2), 1)
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)
        self.assertEqual(self.calc.divide(1000000, 1000), 1000.0)

    def test_very_small_numbers(self):
        """Test operations with very small decimal numbers."""
        small_num1 = 0.001
        small_num2 = 0.002
        
        self.assertAlmostEqual(self.calc.add(small_num1, small_num2), 0.003)
        self.assertAlmostEqual(self.calc.subtract(small_num2, small_num1), 0.001)
        self.assertAlmostEqual(self.calc.multiply(small_num1, 1000), 1.0)
        self.assertAlmostEqual(self.calc.divide(small_num2, small_num1), 2.0)


if __name__ == '__main__':
    unittest.main()