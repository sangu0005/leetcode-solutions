class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
            
        res = 0
        for n in str(num):
            res += int(n)

        if 1 <= res <= 9:
            return res
        else:
            return self.addDigits(res) 