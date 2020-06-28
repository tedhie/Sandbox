import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tets for 'name_function.py'"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('seymour', 'skinner')
        self.assertEqual(formatted_name, 'Seymour Skinner')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('lisa', 'simpson', 'marie')
        self.assertEqual(formatted_name, 'Lisa Marie Simpson')

if __name__ == '__main__':
    unittest.main()
