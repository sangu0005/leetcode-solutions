class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        s = set(nums)

        res = []
        for n in range(mini, maxi + 1):
            if n not in s:
                res.append(n)
        return res

