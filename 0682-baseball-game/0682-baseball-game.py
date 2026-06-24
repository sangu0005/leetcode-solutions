class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for ch in operations: 
            if ch == "C" and stk:
                stk.pop()
            elif ch == "D" and stk:
                stk.append(stk[-1]*2)
            elif ch == "+" and len(stk) >= 2:
                stk.append(stk[-1] + stk[-2])
            else:
                 stk.append(int(ch))

        return sum(stk)
