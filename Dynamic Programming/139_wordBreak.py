class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) # d[i] is True if there is a word in the dictionary that ends at ith index of s 

        for i in range(len(s)):
            for w in wordDict:
                start = i - len(w)+1
                # if find w and (the word in s before w is also found or w is the first found word in s)
                if s[start: i+1] == w and (dp[i-len(w)] == True or i-len(w) == -1):
                    dp[i] = True
        return dp[-1]