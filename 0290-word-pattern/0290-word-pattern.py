class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = {}
        words = s.split()
        if len(pattern) != len(words):
            return False

        used = set()
        for i, ch in enumerate(pattern):
            if ch in mp:
                if mp[ch] != words[i]:
                    return False
            else:
                if words[i] in used:
                    return False
                mp[ch] = words[i]
                used.add(words[i])

        return True
        

