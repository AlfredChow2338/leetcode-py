from typing import List

# Runtime: 30 ms, faster than 91.18% of Python3 online submissions for Plus One.
# Memory Usage: 16.5 MB, less than 66.79% of Python3 online submissions for Plus One.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        res = []
        for i, n in enumerate(digits):
            num += n * pow(10, len(digits) - i - 1)
        num += 1
        numStr = str(num)
        for c in numStr:
            res.append(int(c))
        return res
            
        