from simple_calculator import SimpleCalculator
import unittest

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(2, -3), -1)
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-2, 3), -5)
        self.assertEqual(self.calc.subtract(2, -3), 5)
        self.assertEqual(self.calc.subtract(-2, -3), 1)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_division(self):
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-3, 2), -1.5)
        self.assertEqual(self.calc.divide(3, -2), -1.5)
        self.assertEqual(self.calc.divide(-3, -2), 1.5)

if __name__ == "__main__":
    unittest.main()
