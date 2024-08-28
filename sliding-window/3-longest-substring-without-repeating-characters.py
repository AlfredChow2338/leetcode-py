# Runtime: 56 ms, faster than 54.55% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 16.7 MB, less than 39.84% of Python3 online submissions for Longest Substring Without Repeating Characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
            seen[char] = r

        return length