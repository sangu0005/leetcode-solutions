class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # maxCount = 0
        # for s in sentences:
        #     s = s.split()
        #     maxCount = max(maxCount, len(s))
        
        # return maxCount

        maxCount = 0
        for s in sentences:
            wordCount = s.count(' ') + 1
            maxCount = max(maxCount, wordCount)

        return maxCount
