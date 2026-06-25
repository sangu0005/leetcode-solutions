class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hashmap = {}

        for i in range(len(s)):
            hashmap[indices[i]] = s[i]

        res = []

        for i in range(len(s)):
            res.append(hashmap[i]) 

        return "".join(res)