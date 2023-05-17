class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # dp[i][j] mean the max subset num with i zeros and j ones

        for s in strs:
            zero_num = s.count('0')
            one_num = len(s) - zero_num

            for i in range(m,zero_num-1,-1):
                for j in range(n, one_num-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero_num][j-one_num]+1)
                    # dp[i-zero_num][j-zero_num]+1 == the dp[i-zero_num][j-zero_num] + current string s
        
        return dp[m][n]