from typing import List

# Two Pointers
# Runtime: 735 ms, faster than 57.95% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 27.4 MB, less than 35.53% of Python3 online submissions for Best Time to Buy and Sell Stock.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, l, r = 0, 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                res = max(res,profit)
            else:
                l = r
            r += 1
        return res if res >= 0 else 0
            
        