from typing import List

# Prefix Sum
# Runtime: 132 ms, faster than 11.57% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 18.5 MB, less than 41.67% of Python3 online submissions for Trapping Rain Water.
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        a = [0] * len(height)
        b = [0] * len(height)
        
        for i in range(len(height)):
            if i == 0:
                a[i] = height[i]
            else:    
                a[i] = max(height[i], a[i-1])
        
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                b[i] = height[i]
            else:
                b[i] = max(height[i], b[i+1])
    
        
        for i in range(len(height)):
            res += min(a[i], b[i]) - height[i]
                
        return res
                

            
            