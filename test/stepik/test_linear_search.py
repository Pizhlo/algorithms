import unittest
from linear_search.linear_search import linear_search, linear_search_few_values

class TestLinearSearch(unittest.TestCase):

    def test_linear_search(self):
        self.assertEqual(linear_search([1,2,3,4], 4), 3)
        self.assertEqual(linear_search([13, 10, 8, 7, 6, 2, 4, 5, 22], 7), 3)
        self.assertEqual(linear_search([13, 10, 8, 7, 6, 2, 4, 5, 22], 22), 8)
        self.assertEqual(linear_search([13, 10, 8, 7, 6, 2, 4, 5, 22], 100), -1)
        self.assertEqual(linear_search([13, 10, 8, 7, 6, 2, 4, 5, 22], 13), 0)
        self.assertEqual(linear_search([13, 10, 8, 7, 6, 2, 4, 5, 22], 2), 5)

class TestLinearSearchFewValues(unittest.TestCase):

    def test_linear_search_few_values(self):
        self.assertEqual(linear_search_few_values([1,2,3,4], 4), [3])
        self.assertEqual(linear_search_few_values([1, 2, 3, 3, 4, 5], 3), [2, 3])
        self.assertEqual(linear_search_few_values([1, 1, 1, 1, 1], 1), [0, 1, 2, 3, 4])
        self.assertEqual(linear_search_few_values([13, 10, 8, 7, 7, 6, 2, 4, 7, 5, 22], 7), [3, 4, 8])
        self.assertEqual(linear_search_few_values([13, 10, 8, 7, 6, 2, 4, 5, 22], 25), -1)
        self.assertEqual(linear_search_few_values([13, 5, 4, 9, 13, 15, 20], 13), [0, 4])

if __name__ == '__main__':
    unittest.main()