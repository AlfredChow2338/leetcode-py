from typing import List

# Runtime: 84 ms, faster than 37.78% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 16.9 MB, less than 61.65% of Python3 online submissions for Median of Two Sorted Arrays.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B
            
            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i+1] if (i+1) < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j+1] if (j+1) < len(B) else float('infinity')
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2: # odd
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: # too many elements from A
                r = i - 1
            else:
                l = i + 1
        

