from typing import List

# Runtime: 446 ms, faster than 41.16% of Python3 online submissions for Max Consecutive Ones III.
# Memory Usage: 17 MB, less than 68.71% of Python3 online submissions for Max Consecutive Ones III.
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros, res, l = 0, 0, 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res
            
        