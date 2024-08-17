from typing import List

# Sliding Windows
# Runtime: 645 ms, faster than 14.09% of Python3 online submissions for Contiguous Array.
# Memory Usage: 22.1 MB, less than 35.45% of Python3 online submissions for Contiguous Array.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        res = 0
        diff_index_map = {} # count[1] - count[0] -> position (index)
        
        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
                
            if one - zero not in diff_index_map:
                diff_index_map[one - zero] = i
            
            if one == zero:
                res = one + zero
            elif one - zero in diff_index_map:
                idx = diff_index_map[one - zero]
                res = max(res, i - idx)
        
        return res