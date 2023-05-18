class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        if k > n/2: # can not buy and sell at same day
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i-j>0)

        dp = [[0 for _ in range(n)] for _ in range(k+1)]

        for i in range(1,k+1):
            local_max = dp[i-1][0] - prices[0]
            for j in range(1,n):
                dp[i][j] = max(dp[i][j-1], prices[j] + local_max)
                local_max = max(local_max, dp[i-1][j] - prices[j])
        
        return dp[-1][-1]

# For example, if j == 8, then amongst all jj == 1,2,...,7
# The max profit could be one of the following:
# dp[i-1][0] + prices[8] - prices[0]
# dp[i-1][1] + prices[8] - prices[1]
# dp[i-1][2] + prices[8] - prices[2]
# ...
# dp[i-1][6] + prices[8] - prices[6]
# dp[i-1][7] + prices[8] - prices[7]

# localMax is the max value amongst all:
# dp[i-1][0] - prices[0]
# dp[i-1][1] - prices[1]
# dp[i-1][2] - prices[2]
# ...
# dp[i-1][6] - prices[6]
# dp[i-1][7] - prices[7] 

# Then localMax + prices[8] is the max profit if we sell the stock at day 8. Then we compare this result with the max profit of not selling the stock at day 8, take the max of the two.