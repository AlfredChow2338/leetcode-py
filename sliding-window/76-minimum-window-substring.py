# Runtime: 98 ms, faster than 86.34% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 17.3 MB, less than 78.06% of Python3 online submissions for Minimum Window Substring.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT, window = {}, {}
        
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                currLen = r - l + 1
                if currLen < resLen:
                    res = [l, r]
                    resLen = currLen
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        print(res, resLen)
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
                
        
        