class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total = 0
        count = [0] * 101

        for num in nums:
            count[num] += 1

        for i in range(1, 101):
            if count[i] == 1:
                total += i
        
        return total