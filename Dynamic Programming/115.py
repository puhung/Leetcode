class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        
        for i in range(1, m+1): 
            for j in range(1, n+1): 
                dp[i][j] = dp[i-1][j] # example: when t = "rab", s = "rabb", dp[i-1][j] represents the case t = "rab", s = "rab"
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1] # example: when t = "rab", s = "rabb", dp[i-1][j-1] represents the case t = "ra", s = "rab"
        return dp[-1][-1]