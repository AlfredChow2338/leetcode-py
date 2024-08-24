from typing import List

# Runtime: 44 ms, faster than 68.22% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 17.1 MB, less than 61.21% of Python3 online submissions for Search a 2D Matrix.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(l: List[int], start: int, end: int) -> bool:
            if start > end:
                return False
            mid = (start + end) // 2
            if l[mid] == target:
                return True
            if l[mid] > target:
                return bs(l, start, mid - 1)
            if l[mid] < target:
                return bs(l, mid + 1, end)
            
        for l in matrix:
            res = bs(l, 0, len(l) - 1)
            if res:
                return res
        return False