from django.test import SimpleTestCase
from app import calc


class test_calc(SimpleTestCase):
    """Test the add function from calc.py"""
    def test_add(self):
        res = calc.add(3, 8)
        self.assertEqual(res, 11)
