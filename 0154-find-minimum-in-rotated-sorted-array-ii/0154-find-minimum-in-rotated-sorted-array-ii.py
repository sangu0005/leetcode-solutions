class Solution:
    def findMin(self, nums: List[int]) -> int:
        u_nums = []
        for num in nums:
            if num not in u_nums:
                u_nums.append(num)

        l, r = 0, len(u_nums)-1

        while l < r:
            mid = (l + r) // 2

            if u_nums[mid] > u_nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return u_nums[l]