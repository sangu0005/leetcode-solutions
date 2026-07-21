class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        points.sort(key = lambda p : p[0]**2 + p[1]**2)

        for x,y in points:
            res.append([x,y])
            k -= 1
            if k == 0:
                break
        return res
