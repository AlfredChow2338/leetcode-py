from typing import List

# Loop by condition
# Runtime: 262 ms, faster than 77.98% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 25.7 MB, less than 47.43% of Python3 online submissions for Product of Array Except Self.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_nums = 0
        res = []
        
        for n in nums:
            total_product *= n;
            
            if n == 0:
                zero_nums += 1
        
        for n in nums:
            if zero_nums >= 2:
                return [0 for i in range(len(nums))]
            
            if zero_nums == 1:
                if n == 0:
                    a = 1
                    for m in nums:
                        if (m != 0): 
                            a *= m
                    res.append(a)
                else:
                    res.append(0)
                    
            else:
                res.append(int(total_product / n))
        
        return res