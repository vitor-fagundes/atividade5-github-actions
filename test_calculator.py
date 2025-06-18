import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(calculator.divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
