class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)

        # dp[i][j] means whether the specific sum j can be gotten from the first i numbers
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]
        dp[0][0] = True

        for i in range(1, n+1):
            cur_num = nums[i-1]
            for j in range(target+1):
                if j < cur_num:
                    dp[i][j] = dp[i-1][j] # if sum j is smaller than cur_num, we can not use cur_num to get j
                else:
                    # if sum j is greater than cur_num, we can choose to use or not to use cur_num to get j
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-cur_num]
        return dp[n][target]