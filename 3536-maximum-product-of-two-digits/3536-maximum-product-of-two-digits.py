class Solution:
    def maxProduct(self, n: int) -> int:
        first, second = 0, 0
        
        while n != 0:
            ld = (n % 10)
            n //= 10

            if ld > first:
                second = first
                first = ld
            elif ld >  second:
                second = ld
        
        return first * second