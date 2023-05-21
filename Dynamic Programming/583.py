class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[1000 for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(n1+1):
            for j in range(n2+1):
                if i == 0 or j == 0:
                    dp[i][j] = i+j
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]