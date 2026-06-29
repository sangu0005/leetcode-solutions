class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # for i in range(n):
        #     min_index = i
        #     for j in range(i+1, n):
        #         if nums[j] < nums[min_index]:
        #             min_index = j
        #     nums[i], nums[min_index] = nums[min_index], nums[i] 

        low = mid = 0
        high = len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            