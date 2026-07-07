class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res = 0
        total = 0
        for i in str(n):
            if i != '0':
                total += int(i)
                res = (res * 10) + int(i)
        return int(total) * res

