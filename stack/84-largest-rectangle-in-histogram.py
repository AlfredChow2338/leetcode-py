from typing import List

# Runtime: 660 ms, faster than 70.13% of Python3 online submissions for Largest Rectangle in Histogram.
# Memory Usage: 33.7 MB, less than 25.41% of Python3 online submissions for Largest Rectangle in Histogram.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        st = [] # [ pair: (index, height), ... ]
        
        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                idx, height = st.pop()
                maxA = max(maxA, height * (i - idx))
                start = idx
            st.append((start, h))
        
            
        for i, h in st:
            maxA = max(maxA, h * (len(heights) - i))
        
        return maxA