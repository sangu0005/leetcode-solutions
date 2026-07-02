class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)

        diff = 0

        for ch in s_count:
            if s_count[ch] > t_count[ch]:
                diff += s_count[ch] - t_count[ch]

        return diff