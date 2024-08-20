from typing import List

# Prefix Sum
# Runtime: 638 ms, faster than 79.75% of Python3 online submissions for 3Sum.
# Memory Usage: 20.7 MB, less than 31.50% of Python3 online submissions for 3Sum.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res
  
# Two Pointers
# Runtime: 124 ms, faster than 16.98% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 18.4 MB, less than 41.67% of Python3 online submissions for Trapping Rain Water.
class Solution:
    def trap(self, height: List[int]) -> int:
        res, l, r, maxL, maxR = 0, 0, len(height) - 1, height[0], height[len(height)-1]
        
        while l < r:
            if l > 0:
                maxL = max(maxL, height[l])
            
            if r < len(height) -1:
                maxR = max(maxR, height[r])
            
            if maxL <= maxR:
                l += 1
                temp = min(maxL, maxR) - height[l]
                if temp > 0:
                    res += temp
            else:
                r -= 1
                temp = min(maxL, maxR) - height[r]
                if temp > 0:
                    res += temp
                
        return res