class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        
        for i in range(0, n+1):
            for j in range(0, n+1):
                if i+j <= n:
                    ss = s[j:j+i]
                    if '0' in ss or '1' in ss:
                        zero =  ss.count('0')
                        one = ss.count('1')

                        if zero <= k or one <= k:
                            res += 1

        return res