class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = {}
        for n in arr:
            mp[n] = mp.get(n, 0) + 1
         
        maxi = 0
        for k, v in mp.items():
            if k == v:
                if k > maxi:
                    maxi = k
        return maxi if maxi else -1