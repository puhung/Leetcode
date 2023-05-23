class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    pos = stack.pop()
                    dp[i+1] = dp[pos] + (i-pos+1) 
                    # dp[pos] is the longest valid parentheses substring before the '('
                    # then we add the distance between ') ' and '(': i-pos+1

        return max(dp)