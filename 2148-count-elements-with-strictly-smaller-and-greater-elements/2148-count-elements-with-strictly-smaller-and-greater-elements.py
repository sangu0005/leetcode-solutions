class Solution:
    def countElements(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)

        return sum(mn < n < mx for n in nums )
        # mn = min(nums)
        # mx = max(nums)
        # cnt = 0

        # for n in nums:
        #     if n > mn and n < mx:
        #         cnt += 1

        # return cnt