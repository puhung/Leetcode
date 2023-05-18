class Solution:
    def minSteps(self, n: int) -> int:
        dp = [i for i in range(n+1)] # minimum step to get i on screen 
        dp[1] = 0 # since the base case would be one 'A' on screen

        for i in range(2,n+1):
            # find the largest factor that can divide i
            for factor in range(i//2, 0, -1):
                if i % factor == 0:
                    # + 1 = copy the factor 'A' on screen 
                    # paste the factor 'A' (i//factor - 1) times.
                    # dp[8] = dp[4] + 1 + (8//2-1)
                    dp[i] = dp[factor] + 1 + (i//factor - 1)
                    break
        
        return dp[-1]