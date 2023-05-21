class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0] * 2 for _ in range(len(prices)+1)  ]
        
        for i in range(len(prices)-1, -1, -1):
            for j in range(2):
                
                if j == 0: #sell
                    dp[i][j] = max(dp[i+1][j], dp[i+1][1] + prices[i] -fee) # stay the same or sell the stock (buy + prices[i] - fee)
                else: # buy
                    dp[i][j] = max(dp[i+1][j], dp[i+1][0] - prices[i]) # stay the same or buy the stock (sell - prices[i])
                    
        return dp[0][1] # since when i = 0, it is the start of the dp, we must buy instead of sell