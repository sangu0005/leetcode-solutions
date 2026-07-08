class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [""] * len(score)
        s = sorted(range(len(score)), key = lambda i : -score[i])
        for rank, i in enumerate(s, 1):
            if rank == 1:
                res[i] = "Gold Medal"
            elif rank == 2:
                res[i] = "Silver Medal"
            elif rank == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(rank)
        return res
