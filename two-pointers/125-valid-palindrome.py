# clean text
# Runtime: 41 ms, faster than 77.63% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 17.3 MB, less than 41.11% of Python3 online submissions for Valid Palindrome.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join(char for char in s if char.isalnum()).lower()
        
        left = 0
        right = len(t) - 1
        
        while left <= right:
            if t[left] != t[right]:
                return False
            left += 1
            right -= 1
        
        return True