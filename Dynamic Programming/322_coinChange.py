class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for i in range(1, amount+1):
            dp[i] = 1 + min(dp[i-c] if i-c >= 0 else float('inf') for c in coins)

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]