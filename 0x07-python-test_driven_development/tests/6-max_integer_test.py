#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_signed_ints_and_floats(self):
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 4, 1]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_None(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)


if __name__ == "__main__":
    unittest.main()
