
from typing import List

# Brute Force
# Time Limit Exceeded
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        l, r = 0, 1
        day = 0
            
        while l < len(temperatures):
            if temperatures[r] > temperatures[l]:
                day += 1
                res.append(day)
                l += 1
                r = l + 1 if l != len(temperatures) - 1 else l
                day = 0
            
            else:
                if r == len(temperatures) - 1:
                    if temperatures[r] > temperatures[l]:
                        res.append(day)
                    else: 
                        res.append(0)
                        
                    l += 1
                    r = l + 1 if l != len(temperatures) - 1 else l
                        
                    day = 0
                else:
                    day += 1
                    r += 1
        return res

# Stack + Hashmap  
# Runtime: 1411 ms, faster than 5.04% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 46.4 MB, less than 5.37% of Python3 online submissions for Daily 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        
        for i in range(len(temperatures)):
            st.append({ temperatures[i]: i })
            
            for j in range(len(st) - 1, -1, -1):
                if i == len(temperatures) - 1:
                    return res
                if temperatures[i+1] > list(st[j].keys())[0]:
                    res[list(st[j].values())[0]] = i - list(st[j].values())[0] + 1
                    st.pop()   
                else:
                    break
                    
        return res

# Stack            
# Runtime: 1042 ms, faster than 5.04% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 30.7 MB, less than 85.20% of Python3 online submissions for Daily 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = [] # [index, value, index, value, ...]
        
        for i in range(len(temperatures)):
            st.append(i)
            st.append(temperatures[i])
            
            for j in range(len(st) - 1, -1, -2):
                if i == len(temperatures) - 1:
                    return res
                if temperatures[i+1] > st[j]:
                    res[st[j-1]] = i - st[j-1] + 1
                    st.pop()
                    st.pop()
                else:
                    break
                    
        return res
            
# Monotonic Decreasing Stack
# Runtime: 906 ms, faster than 34.10% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 32.1 MB, less than 19.42% of Python3 online submissions for Daily Temperatures.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = [] # [[index, value], [index, value], ...]
        
        for i, t in enumerate(temperatures):
            while st and t > st[-1][1]:
                idx, val = st.pop()
                res[idx] = i - idx
            st.append([i, t])
                    
        return res
            