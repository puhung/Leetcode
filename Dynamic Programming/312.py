class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        
        def dfs(l, r):
            if l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            
            coin = 0
            for i in range(l, r+1):
                coin = max(coin, dfs(l, i-1) + nums[l-1] * nums[i] *nums[r+1] +  dfs(i+1, r))

            dp[(l,r)] = coin
            return dp[(l,r)]
        
        return dfs(1, len(nums)-2)

# Time complexity: O(N^3). There are O(N^2) states. For each state, determining the maximum coins requires iterating over all balloons in the range [left, right]. Thus the total time complexity is O(N^2)×O(N)=O(N^3)