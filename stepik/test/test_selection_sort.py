import unittest
from selection_sort.selection_sort import selection_sort

class TestSum(unittest.TestCase):

    def test_selection_sort(self):
        self.assertEqual(selection_sort([7, 8, 2, 5, 3, 6, 1, 9]), [1, 2, 3, 5, 6, 7, 8, 9])
        self.assertEqual(selection_sort([1, 2, 3, 4, 5, 6, 7, 8]), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(selection_sort([2, 8, 7, 5, 3, 6]), [2, 3, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()
