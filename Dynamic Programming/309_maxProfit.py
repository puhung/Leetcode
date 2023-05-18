class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        cool_down, sell, hold = 0, 0, float('-inf')

        for price in prices:
           prev_cool, prev_sell, prev_hold = cool_down, sell, hold

           cool_down = max(prev_cool, prev_sell) # Max profit of cooldown on Day i comes from either cool down of Day_i-1, or sell out of Day_i-1 and today Day_i is cooling day
           sell = prev_hold + price  # Max profit of sell on Day_i comes from hold of Day_i-1 and sell on Day_i
           hold = max(prev_hold, prev_cool - price) # Max profit of hold on Day_i comes from either hold of Day_i-1, or cool down on Day_i-1 and buy on Day_i

        return max(sell, cool_down)