class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def isPali(start, end):
            if start >= end:
                return True
            if s[start] != s[end]:
                return False
            return isPali(start+1, end-1)

        @lru_cache(None)
        def dp(start):
            if start == n:
                return 0

            res = float('inf')
            for end in range(start, n):
                if isPali(start,end):
                    next_start = end+1
                    res = min(res, dp(next_start) + 1)
            return res
        
        return dp(0)-1 # -1 is to reduce the unnecessary cut