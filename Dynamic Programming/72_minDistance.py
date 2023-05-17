class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # dp[i][j] represent the minimum number to change to make word1 same as word2
        # when i and j equal to the numbers left in the word1 and word2

        for i in range(m+1):
            dp[i][0] = i
        
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                # the letters are the same
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] # nothing need to do
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    # dp[i-1][j-1] -> we need to replace the letters
                    # dp[i-1][j], dp[i][j-1] -> we need to delete word1[i-1] or word2[j-1]
        
        return dp[m][n]