class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l = sorted(arr)
        mp = {}
        rank = 1
        for i,n in enumerate(l):
            if n not in mp:
                mp[n] = rank
                rank += 1

        res = []
        for j in arr:
            res.append(mp[j])
        return res