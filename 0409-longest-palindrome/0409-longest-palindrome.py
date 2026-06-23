class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        length = 0
        has_odd = 0

        for cnt in count.values():
            if cnt % 2 == 0:
                length += cnt
            else:
                length += cnt-1
                has_odd = 1
        
        return length + has_odd