import unittest
import random
from stepik.selection_sort.selection_sort import selection_sort

class TestSelectionSort(unittest.TestCase):

    def test_selection_sort(self):
        random_list = self.generate()
        sorted_list = sorted(random_list)

        self.assertEqual(selection_sort(random_list), sorted_list)

    def generate(self) -> list[int]:
        """
        Генерирует тестовые данные.
        """
        random_list = []
        for i in range(0, 100):
            n = random.randint(1, 1_000_000)
            random_list.append(n)
        return random_list

if __name__ == '__main__':
    unittest.main()
