class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # squares = set()

        # for i in range(int(c**0.5)+1):
        #     squares.add(i*i)
        
        # for square in squares:
        #     if c - square in squares:
        #         return True
        # return False

        l = 0
        r = int(c ** 0.5)
        while l <= r:
            total = (l*l) + (r*r)
            if total == c:
                return True
            elif total < c:
                l += 1
            else:
                r -= 1
        return False
