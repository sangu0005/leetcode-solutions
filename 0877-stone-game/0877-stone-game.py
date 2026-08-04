class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice = 0
        bob = 0
        l = 0
        r = len(piles) - 1

        while l <= r:
            if piles[l] < piles[r]:
                alice += piles[r]
                r -= 1
                if piles[l] > piles[r]:
                    bob += piles[r]
                    r -= 1
                else:
                    bob += piles[l]
                    l += 1
            else:
                alice += piles[l]
                l += 1
        
        return alice > bob