class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l = sorted(set(arr))
        mp = {}
        rank = 1
        for n in l:
            mp[n] = rank
            rank += 1
        res = []
        for j in arr:
            res.append(mp[j])
        return res