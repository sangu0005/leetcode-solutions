class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                
            seen.add(s[r])
            res = max(res, r-l+1)

        return res

        # res = 0
        # for i in range(len(s)):
        #     for j in range(i + 1 , len(s) + 1):
        #         sub = s[i : j]
        #         if len(sub) == len(set(sub)):
        #             res = max(res, len(sub))
        # return res