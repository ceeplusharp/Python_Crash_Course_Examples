# Chapter 11: Try It Yourself: 11-01. City, Country, Test Case

import unittest
from pcc_1101_city_country_function import get_city_country


class NamesTestCase(unittest.TestCase):
    """Tests for 'pcc_1101_city_country_function'."""

    def test_city_country(self):
        """Does input like Manila Philippines work?"""
        formatted_city = get_city_country('manila', 'philippines')
        self.assertEqual(formatted_city, 'Manila, Philippines')


if __name__ == '__main__':
    unittest.main()
