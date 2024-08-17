from typing import List

# Prefix Sum
# Runtime: 220 ms, faster than 86.05% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 19.4 MB, less than 54.72% of Python3 online submissions for Subarray Sum Equals K.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        prefixSums = { 0: 1 } # currSum -> count
        
        for n in nums:
            currSum += n
            diff = currSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
        
        return res