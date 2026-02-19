import unittest
import calculator
import os

class TestCalculator(unittest.TestCase):

    def setUp(self):
        calculator.HISTORY_FILE = "test_history.txt"
        calculator.history = []
        if os.path.exists(calculator.HISTORY_FILE):
            os.remove(calculator.HISTORY_FILE)

    def tearDown(self):
        if os.path.exists(calculator.HISTORY_FILE):
            os.remove(calculator.HISTORY_FILE)

    def test_parse_string_calculation(self):
        self.assertEqual(calculator.parse_string_calculation("2+2"), [2, '+', 2])
        self.assertEqual(calculator.parse_string_calculation("2-2"), [2, '-', 2])
        self.assertEqual(calculator.parse_string_calculation("2*2"), [2, '*', 2])
        self.assertEqual(calculator.parse_string_calculation("2/2"), [2, '/', 2])
        self.assertEqual(calculator.parse_string_calculation("2.5+2.5"), [2.5, '+', 2.5])
        self.assertEqual(calculator.parse_string_calculation("-2+2"), [-2, '+', 2])
        self.assertEqual(calculator.parse_string_calculation("2+-2"), [2, '+', -2])
        self.assertEqual(calculator.parse_string_calculation("abc"), [])

    def test_priority_calculation_basic(self):
        self.assertEqual(calculator.priority_calculation([2, '+', 2]), 4)
        self.assertEqual(calculator.priority_calculation([5, '-', 3]), 2)
        self.assertEqual(calculator.priority_calculation([4, '*', 2]), 8)
        self.assertEqual(calculator.priority_calculation([10, '/', 2]), 5)

    def test_priority_calculation_order(self):
        # 2 + 3 * 4 = 14
        self.assertEqual(calculator.priority_calculation([2, '+', 3, '*', 4]), 14)
        # 10 - 2 * 3 = 4
        self.assertEqual(calculator.priority_calculation([10, '-', 2, '*', 3]), 4)
        # 10 / 2 + 3 = 8
        self.assertEqual(calculator.priority_calculation([10, '/', 2, '+', 3]), 8)

    def test_priority_calculation_floats(self):
        self.assertAlmostEqual(calculator.priority_calculation([2.5, '+', 2.5]), 5.0)
        self.assertAlmostEqual(calculator.priority_calculation([5, '/', 2]), 2.5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.priority_calculation([1, '/', 0])

    def test_invalid_input(self):
        # Empty input
        with self.assertRaisesRegex(ValueError, "Invalid calculation: Empty input"):
            calculator.priority_calculation([])

        # Missing operand at end
        with self.assertRaisesRegex(ValueError, "Invalid operator placement"):
            calculator.priority_calculation([2, '+'])

        # Missing operand at start
        with self.assertRaisesRegex(ValueError, "Invalid operator placement"):
            calculator.priority_calculation(['+', 2])

        # Missing operator in between
        with self.assertRaisesRegex(ValueError, "Invalid calculation structure"):
            calculator.priority_calculation([2, 2])

        # Consecutive operators (e.g., 2 + + 2) -> parsed as [2, '+', '+', 2]
        with self.assertRaisesRegex(ValueError, "Invalid operands"):
             calculator.priority_calculation([2, '+', '+', 2])

    def test_history(self):
        calculator.add_to_history("2+2", 4)
        self.assertIn("2+2 = 4", calculator.history)

        with open(calculator.HISTORY_FILE, "r") as f:
            content = f.read()
        self.assertIn("2+2 = 4", content)

if __name__ == '__main__':
    unittest.main()
