# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# https://leetcode.com/problems/search-insert-position/description/

def search_insert(nums: list, target: int) -> int:
        first = 0
        last = len(nums) - 1
        while first <= last:
            middle = (first + last) // 2
            if nums[middle] < target:
                first = middle + 1
            elif nums[middle] > target:
                last = middle - 1
            else:
                return middle


        return first


print(search_insert([1,3,5,6], 4))