class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0

        # fast = 0
        # for i in range(len(nums)):
        #     if i > fast:
        #         return False
        #     fast = max(fast, i + nums[i])
        # return True