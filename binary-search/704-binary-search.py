from typing import List

# while loop
# Runtime: 196 ms, faster than 23.55% of Python3 online submissions for Binary Search.
# Memory Usage: 18.1 MB, less than 67.90% of Python3 online submissions for Binary Search.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            if nums[mid] < target:
                start = mid + 1
        return -1

# recursion
# Runtime: 187 ms, faster than 76.12% of Python3 online submissions for Binary Search.
# Memory Usage: 25.5 MB, less than 28.32% of Python3 online submissions for Binary Search.
class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        def bs(start: int, end: int) -> int:
            if start > end:
                return -1
            
            middle = (start + end) // 2
            
            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                return bs(start, middle - 1)
            
            if nums[middle] < target:
                return bs(middle + 1, end)
        
        return bs(0, len(nums) - 1)
        