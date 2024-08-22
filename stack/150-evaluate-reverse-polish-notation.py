from typing import List

# Stack
# Runtime: 62 ms, faster than 77.33% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 17.2 MB, less than 14.09% of Python3 online submissions for Evaluate Reverse Polish Notation.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = ['+', '-', '*', '/']
        st = []
        
        def cal(a: str, b: str, op: str) -> str:
            intA, intB = int(a), int(b)
            if op == '+':
                return intA + intB 
            elif op == '-':
                return intA - intB 
            elif op == '*':
                return intA * intB 
            elif op == '/':
                return intA / intB 
            else:
                return 0
        
        for i, c in enumerate(tokens):
            if c in symbols:
                lastOne = st.pop()
                lastTwo = st.pop()
                result = cal(lastTwo, lastOne, c)
                st.append(result)
            else:
                st.append(c)
    
        return st[0]