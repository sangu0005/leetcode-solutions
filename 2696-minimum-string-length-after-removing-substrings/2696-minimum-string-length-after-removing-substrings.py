class Solution:
    def minLength(self, s: str) -> int:
        stk = []

        for ch in s:
            if stk and ((stk[-1] == "A" and ch == "B") or (stk[-1] == "C" and ch == "D")):
                stk.pop()
            else:
                stk.append(ch)
        
        return len(stk)