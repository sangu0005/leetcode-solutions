class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * (n)
        stk = []

        for i, temp in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < temp:
                prev_day = stk.pop()
                res[prev_day] = i - prev_day
            stk.append(i)
            
        return res
