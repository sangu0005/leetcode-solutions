class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = list(map(str, nums)) # to convert all numbers to strings
        nums.sort(key = lambda x : x * 10, reverse = True)
        # res = "".join(nums)
        # return "0" if res[0] == "0" else res

        if nums[0] == "0":
            return "0"
        
        return "".join(nums)