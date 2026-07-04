# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:

        # stk1 = []
        # stk2 = []

        # for ch in s:
        #     if stk1 and ch == "#":
        #         stk1.pop()
        #     else:
        #         if ch != "#":
        #             stk1.append(ch)

        # for ch in t:
        #     if stk2 and ch == "#":
        #         stk2.pop()
        #     else:
        #         if ch != "#":
        #             stk2.append(ch)
        
        # return stk1 == stk2
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def build(string):
            stk = []

            for ch in string:
                if ch != "#":
                    stk.append(ch)
                else:
                    if stk:
                        stk.pop()
            return stk

        return build(s) == build(t)