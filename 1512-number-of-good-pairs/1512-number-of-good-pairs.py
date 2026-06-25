class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # res = 0

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if i < j and nums[i] == nums[j]:
        #             res += 1
        # return res

        hashmap = {}
        res = 0

        for num in nums:
            if num in hashmap:
                res += hashmap[num]
            hashmap[num] = hashmap.get(num, 0) +1

        return res