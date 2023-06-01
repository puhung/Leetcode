class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)] # dp[i][j] represents whether s[:i] and p[:j] matches
        dp[0][0] = True # empty s and empty p must match
        
        for j in range(1,len(p)+1):
            if p[j-1] != "*":
                break
            else:
                dp[0][j] = True
        
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] in {s[i-1], "?"}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j] # dp[i][j-1]: "*" represents empty /  dp[i-1][j]: "*" represents s[i-1] + other sequence
                
        return dp[-1][-1]