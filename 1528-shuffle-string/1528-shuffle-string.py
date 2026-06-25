class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ""
        hashmap = {}

        for i in range(len(s)):
            hashmap[indices[i]] = s[i]

        for i in range(len(s)):
            res += hashmap[i] 

        return res