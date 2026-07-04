class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        j = 0

        for x in pushed:
            stk.append(x)

            while stk and j < len(popped) and stk[-1] == popped[j]:
                stk.pop()
                j += 1
        
        return j == len(popped)