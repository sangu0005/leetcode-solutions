class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # total = 0
        # count = [0] * 101

        # for num in nums:
        #     count[num] += 1

        # for i in range(1, 101):
        #     if count[i] == 1:
        #         total += i
        
        # return total

        total = 0
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for num, count in hashmap.items():
            if count == 1:
                total += num
        
        return total   