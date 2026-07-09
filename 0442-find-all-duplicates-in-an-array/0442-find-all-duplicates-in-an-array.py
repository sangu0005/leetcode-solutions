class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # res = []
        # for n in nums:
        #     n = abs(n)
        #     if nums[n - 1] < 0:
        #         res.append(n)
        #     nums[n - 1] = -nums[n - 1]
        # return res
        res = []

        for n in nums:
            idx = abs(n)
            if nums[idx - 1] < 0:
                res.append(idx)
            else:
                nums[idx - 1] *= -1

        return res