from typing import List

# Brute Force
# Time Limit Exceeded
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)
        
        return res
        
# Two Pointers
# Runtime: 554 ms, faster than 6.87% of Python3 online submissions for Container With Most Water.
# Memory Usage: 29.9 MB, less than 6.79% of Python3 online submissions for Container With Most Water.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(area, res)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res
        
# Two Pointers II
# Runtime: 519 ms, faster than 64.11% of Python3 online submissions for Container With Most Water.
# Memory Usage: 29.5 MB, less than 66.34% of Python3 online submissions for Container With Most Water.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(area, res)
            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else:
                if l + 1 != r and r - 1 != r:
                    if height[l+1] > height[r-1]:
                        r -= 1
                    else:
                        l += 1
                else:
                    l += 1
                        
        return res