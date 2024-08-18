from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(0,len(nums)-k+1):
            isConse = True
            subMax = nums[i]
            for j in range(0,k-1):
                subMax = max(subMax, nums[i+j+1])
                if nums[i+j+1] - nums[i+j] != 1:
                    isConse = False
                
            if isConse:
                res.append(subMax)
            else:
                res.append(-1)
        return res