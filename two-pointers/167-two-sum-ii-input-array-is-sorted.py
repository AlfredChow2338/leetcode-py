from typing import List

# Two Pointers
# Runtime: 111 ms, faster than 22.31% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 17.8 MB, less than 31.64% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        
        while right < len(numbers):
            if numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] < target:
                left += 1
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
                                        
            