class Solution:
    def hammingWeight(self, n: int) -> int:
        res = ''
        while n != 0:
            res += str(n % 2)
            n //= 2
        
        count = 0
        for ch in res:
            if ch == "1":
                count += 1
        return count