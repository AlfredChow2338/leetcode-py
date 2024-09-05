# Runtime: 39 ms, faster than 23.88% of Python3 online submissions for Length of Last Word.
# Memory Usage: 16.6 MB, less than 12.11% of Python3 online submissions for Length of Last Word.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        
        for r in range(len(s) - 1, -1, -1):
            if s[r] == " " and res > 0:
                return res
            if s[r] != " ":
                res += 1
        return res

# Runtime: 38 ms, faster than 31.74% of Python3 online submissions for Length of Last Word.
# Memory Usage: 16.5 MB, less than 58.67% of Python3 online submissions for Length of Last Word.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        
        if not words:
            return 0
        
        return len(words[-1])