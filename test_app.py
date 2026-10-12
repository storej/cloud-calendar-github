"""Тести для застосунку-калькулятора."""

import unittest
from unittest.mock import patch

from app import add, ask_number


class TestAdd(unittest.TestCase):
    def test_add_ints(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_add_negative(self):
        self.assertEqual(add(-5, 3), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)


class TestAskNumber(unittest.TestCase):
    @patch("builtins.input", return_value="5")
    def test_valid_number(self, _):
        self.assertEqual(ask_number("a: "), 5.0)

    @patch("builtins.input", side_effect=["abc", "7"])
    def test_retry_on_invalid(self, _):
        self.assertEqual(ask_number("a: "), 7.0)


if __name__ == "__main__":
    unittest.main()