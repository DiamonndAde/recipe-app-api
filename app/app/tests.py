"""
Sample tests
"""
from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """
    Sample tests
    """

    def test_add_numbers(self):
        """
        Test that two numbers are added together
        """
        # self.assertEqual(calc.add(3, 8), 11)

        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """
        Test that values are subtracted and returned
        """
        res = calc.subtract(5, 11)
        self.assertEqual(res, 6)
