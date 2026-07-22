class Solution:
    def jump(self, nums: List[int]) -> int:
        fast = 0
        curr = 0
        count = 0
        for i in range(len(nums)-1):
            fast = max(fast, i + nums[i])

            if i == curr:
                count += 1
                curr = fast

        return count