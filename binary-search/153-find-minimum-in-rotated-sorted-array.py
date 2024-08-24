from typing import List

# Runtime: 33 ms, faster than 96.61% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 16.7 MB, less than 97.83% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]
        
        if nums[l] <= nums[r]:
            return nums[l]
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else: 
                res = min(res, nums[mid])
                r = mid - 1
        
        return res
        
            
                
            