class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums) # the farest position each idx can reach
        dp[0] = nums[0] # idx0 can reach nums[0] position

        goal = len(nums)-1 # last index

        for i in range(1, len(nums)):
            
            # this means idx i-1 can not reach the current position
            if dp[i-1] < i:
                return False

            dp[i] = max(dp[i-1], i+nums[i])

            if dp[i] >= goal:
                return True
        
        return dp[len(nums) - 2] >= goal # check the last 2 idx can reach goal