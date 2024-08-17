# String Compare
# Runtime: 40 ms, faster than 81.81% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 16.9 MB, less than 97.71% of Python3 online submissions for Valid Palindrome.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ''
        
        for c in s:
            if c.isalnum():
                ns += c.lower()
                
        return ns == ns[::-1]

# Two Pointers
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
    
# Two Pointers II
# Runtime: 66 ms, faster than 6.21% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 17 MB, less than 81.35% of Python3 online submissions for Valid Palindrome.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            
            while l < r and not self.isAlphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
    
    def isAlphaNum (self, c: chr) -> bool:
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9') 
        )