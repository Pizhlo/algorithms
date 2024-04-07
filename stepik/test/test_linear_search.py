import unittest
from linear_search.linear_search import linear_search

class TestLinearSearch(unittest.TestCase):

    def test_selection_sort(self):
        self.assertEqual(linear_search([1,2,3,4], 4), 3)
        self.assertEqual(linear_search([13, 10, 8, 7, 6, 2, 4, 5, 22], 7), 3)
        self.assertEqual(linear_search([13, 10, 8, 7, 6, 2, 4, 5, 22], 22), 8)
        self.assertEqual(linear_search([13, 10, 8, 7, 6, 2, 4, 5, 22], 100), -1)
        self.assertEqual(linear_search([13, 10, 8, 7, 6, 2, 4, 5, 22], 13), 0)
        self.assertEqual(linear_search([13, 10, 8, 7, 6, 2, 4, 5, 22], 2), 5)

if __name__ == '__main__':
    unittest.main()