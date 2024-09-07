from collections import defaultdict

# Runtime: 60 ms, faster than 62.29% of Python3 online submissions for Permutation in String.
# Memory Usage: 16.6 MB, less than 60.29% of Python3 online submissions for Permutation in String.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashtable = defaultdict(int)
        running_hashtable = defaultdict(int)
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            hashtable[s1[i]]+= 1
            if i < len(s1)-1:
                running_hashtable[s2[i]] += 1
        l = 0
        for j in range(len(s1)-1,len(s2)):
            running_hashtable[s2[j]] += 1
            flag = True
            for k,v in running_hashtable.items():
                
                if v>0:
                    if hashtable.get(k,0) != v:
                        flag = False
                        break 
                else:
                    if hashtable[k] > 0:
                        flag = False
                        break 
            if flag:
                return True
            
            running_hashtable[s2[l]] -= 1
            l += 1
        return False

# Alphabetical Count    
# Runtime: 65 ms, faster than 53.18% of Python3 online submissions for Permutation in String.
# Memory Usage: 17 MB, less than 18.30% of Python3 online submissions for Permutation in String.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        matches, l = 0, 0
        s1Count = [0] * 26
        s2Count = [0] * 26
        
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        for r in range(len(s1), len(s2)):
            print(matches)
            if matches == 26: return True        
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] - 1 == s1Count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] + 1 == s1Count[index]:
                matches -= 1
            
            l += 1
        
        return matches == 26