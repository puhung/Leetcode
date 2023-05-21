class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res = 0
        n = len(matrix[0])
        heights = [0] * (n+1) # the last 0 is to pop the remaining in the idx_stack

        for i in range(len(matrix)):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            idx_stack = [-1] # heights[-1] would always be 0

            for i in range(n+1): # remember to iterate n+1, so heights[-1] == 0 would pop all idx in the idx_stack 
                # heights[0] will always >= heights[-1], so there would not be an error
                while heights[i] < heights[idx_stack[-1]]: # [0, 5, 6, 7, 2] -> h*w -> 7 * (4-2-1) or 6 * (4-1-1), or 5 * (4-0-1)
                    h = heights[idx_stack.pop()]
                    w = i - idx_stack[-1] - 1 # -1 is to not count the current i position
                    res = max(res, h*w)
                idx_stack.append(i)
        return res
                    