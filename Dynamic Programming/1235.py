class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        dp = [[0,0]] # inital condition: [endtime, max profit at endtime]

        for s, e, p in jobs:
            # i == the position of the endtime that is smaller than the start time
            # s + 1, since endtime == startTime does not count as overlap
            # - 1 is to find the endtime pos instead of the startTime pos: bisect.bisect(dp, [s+1])
            i = bisect.bisect(dp, [s+1]) - 1 

            # if the profit of choosing the current job > not choosing the current job
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])

        return dp[-1][1]