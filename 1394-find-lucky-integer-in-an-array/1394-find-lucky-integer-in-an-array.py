class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = {}
        for n in arr:
            mp[n] = mp.get(n, 0) + 1
         
        maxi = -1
        for k, v in mp.items():
            if k == v:
                maxi = max(maxi, k)

        return maxi