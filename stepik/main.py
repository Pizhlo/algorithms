arr = [7, 8, 5, 2, 13, 8]
target = 13

def find(arr: list, target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:    
            return i
    return -1

print(find(arr, target))