class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []

        for ch in s:
            if stk and ch.isdigit():
                stk.pop()
            else:
                stk.append(ch)

        return "".join(stk)
