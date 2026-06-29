class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []

        for n in num:
            while stk and k > 0 and stk[-1] > n:
                stk.pop()
                k -= 1
            stk.append(n)
        while k > 0:
            stk.pop()
            k -= 1

        # res = "".join(stk).lstrip("0")
        # return res if res else "0"
        return "".join(stk).lstrip("0") or "0"
