class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = []
        place = 1

        while n != 0:
            d = n % 10
            if d != 0:
                res.append(d * place)
            n //= 10
            place *= 10
        
        return res[ :: -1]
            
