class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = merge_sort(nums[: mid])
            right = merge_sort(nums [mid : ])
            return merge(left,right)
    
        def merge(left, right):
            res = []
            l = r = 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            return res + left[l:] + right[r:]
        return merge_sort(nums)