class Solution:
    def arrangeCoins(self, n: int) -> int:
        # row = 1
        # while row <= n:
        #     n -= row
        #     row += 1
        
        # return row - 1

        l, r = 0, n

        while l <= r:
            mid = (l + r) // 2
            coins = mid * (mid + 1) // 2 # coins need for mid row
            
            if coins == n:
                return mid
            elif coins < n:
                l = mid + 1
            else:
                r = mid - 1

        return r
            
