from calculator import Calculator
import unittest
from math import pi


class TestCalculator(unittest.TestCase):
    def test_checker(self):
        self.calculator = Calculator(5)
        self.assertTrue(self.calculator.checker(5))

    def test_checker_raising_value_error(self):
        self.calculator = Calculator(5)
        self.assertRaises(ValueError, self.calculator.checker, "string")

    def test_iadd(self):
        self.calculator = Calculator(5)
        self.calculator += 2
        self.assertEqual(self.calculator.value, 7)

    def test_isub(self):
        self.calculator = Calculator(5)
        self.calculator -= 2.5
        self.assertEqual(self.calculator.value, 2.5)

    def test_imul(self):
        self.calculator = Calculator(5)
        self.calculator *= 2
        self.assertEqual(self.calculator.value, 10)

    def test_itruediv(self):
        self.calculator = Calculator(5)
        self.calculator /= 3
        self.assertEqual(self.calculator.value, 1.6666666666666667)

    def test_ipow(self):
        self.calculator = Calculator(5)
        self.calculator **= 4
        self.assertEqual(self.calculator.value, 625)

    def test_log10(self):
        self.calculator = Calculator(100.12)
        self.calculator.log10()
        self.assertEqual(self.calculator.value, 2.0005208409361854)

    def test_sqrt_2(self):
        self.calculator = Calculator(100)
        self.calculator.sqrt_2()
        self.assertEqual(self.calculator.value, 10)

    def test_ten_pow(self):
        self.calculator = Calculator(5)
        self.calculator.ten_pow()
        self.assertEqual(self.calculator.value, 100000)

    def test_sqrt_n(self):
        self.calculator = Calculator(27)
        self.calculator.sqrt_n(3)
        self.assertEqual(self.calculator.value, 3)

    def test_exp(self):
        self.calculator = Calculator(2)
        self.calculator.exp()
        self.assertEqual(self.calculator.value, 7.38905609893065)

    def test_sin(self):
        self.calculator = Calculator(90)
        self.calculator.sin()
        self.assertEqual(self.calculator.value, 0.8939966636005579)

    def test_cos(self):
        self.calculator = Calculator(90)
        self.calculator.cos()
        self.assertEqual(self.calculator.value, -0.4480736161291701)

    def test_tan(self):
        self.calculator = Calculator(90)
        self.calculator.tan()
        self.assertEqual(self.calculator.value, -1.995200412208242)

    def test_negate(self):
        self.calculator = Calculator(10)
        self.calculator.negate()
        self.assertEqual(self.calculator.value, -10)

    def test_factorial(self):
        self.calculator = Calculator(5)
        self.calculator.factorial()
        self.assertEqual(self.calculator.value, 120)


if __name__ == "__main__":
    unittest.main()
