class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for word in wordDict:
                if (i + len(word)) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break
        return dp[0]

        # def solve(i = 0):
        #     if i == len(s):
        #         return True
        #     for word in wordDict:
        #         k = len(word)
        #         if s[i : i+k] == word:
        #             if solve(i+k):
        #                 return True
        #     return False
        # return solve()
        



        

