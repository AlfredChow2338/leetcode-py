import math
from typing import List

# Runtime: 277 ms, faster than 37.42% of Python3 online submissions for Koko Eating Bananas.
# Memory Usage: 18.3 MB, less than 14.05% of Python3 online submissions for Koko Eating Bananas.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                print(k)
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
            