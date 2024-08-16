from typing import List

# loop
# Runtime: 2138 ms, faster than 14.30% of Python3 online submissions for Range Sum Query - Immutable.
# Memory Usage: 19.9 MB, less than 89.76% of Python3 online submissions for Range Sum Query - Immutable.
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        r = 0
        for i in range(left, right + 1, 1):
            r += self.nums[i]
        return r
    
# prefix sum
# Runtime: 67 ms, faster than 77.19% of Python3 online submissions for Range Sum Query - Immutable.
# Memory Usage: 20.1 MB, less than 41.17% of Python3 online submissions for Range Sum Query - Immutable.
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if left:
            return self.nums[right] - self.nums[left - 1]
        else: 
            return self.nums[right]