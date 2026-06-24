class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i,num in enumerate(nums):
            if num > 0:
                break
                
            if i > 0 and num == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums)-1
            while l < r:
                threeSum = num + nums[l] + nums[r]

                if threeSum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
                    while l < r and nums[r] == nums [r+1]:
                        r -= 1
                    
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
        return res
