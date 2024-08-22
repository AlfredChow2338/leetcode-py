from typing import List

# Recursion + Stack
# Runtime: 35 ms, faster than 75.49% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 16.8 MB, less than 77.25% of Python3 online submissions for Generate Parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st = []
        res = []
        
        def backTrack(openN: int, closeN: int) -> None:
            print(openN, closeN, st)
            if openN == closeN == n:
                res.append("".join(st))
                return
            
            if openN < n:
                st.append('(')
                backTrack(openN + 1, closeN)
                st.pop()
            
            if openN > closeN:
                st.append(')')
                backTrack(openN, closeN + 1)
                st.pop()
                
        backTrack(0,0)
        
        return res
    
# Recursion + Stack II
# Runtime: 34 ms, faster than 79.40% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 16.7 MB, less than 77.25% of Python3 online submissions for Generate Parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st = []
        res = []
        
        def backTrack(openN: int, closeN: int, s: str) -> None:
            if openN == closeN == n:
                res.append(s)
                return
            
            if openN < n:
                backTrack(openN + 1, closeN, s + '(')
            
            if openN > closeN:
                backTrack(openN, closeN + 1, s + ')')
                
        backTrack(0,0, '')
        
        return res
    