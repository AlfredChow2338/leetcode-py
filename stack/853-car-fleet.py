from typing import List

# Runtime: 750 ms, faster than 27.76% of Python3 online submissions for Car Fleet.
# Memory Usage: 36.7 MB, less than 78.17% of Python3 online submissions for Car Fleet.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        
        for p, s in sorted(pair)[::-1]: # reverse order
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)