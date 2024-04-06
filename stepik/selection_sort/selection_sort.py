def selection_sort(arr: list) -> list:
    """
    Сортировка выбором. 
    Алгоритм берет элемент, находит минимальный и меняет их местами.
    Сложность: O(N^2)
    """

    for i in range(0, len(arr)):
        min_idx = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(arr)

    return arr
        


arr = [7, 8, 2, 5, 3, 6, 1, 9]
arr2 = [1, 2, 3, 4, 5, 6, 7]

if __name__ == '__main__':
    print(selection_sort(arr))