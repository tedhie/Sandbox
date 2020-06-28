import unittest
from city_functions import city_formatter

class NamesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted = city_formatter('västerås', 'sweden')
        self.assertEqual(formatted, "Västerås, Sweden")

    def test_city_country_population(self):
        formatted = city_formatter('västerås', 'sweden', '500000')
        self.assertEqual(formatted, "Västerås, Sweden - Population: 500000")

if __name__ == '__main__':
    unittest.main()