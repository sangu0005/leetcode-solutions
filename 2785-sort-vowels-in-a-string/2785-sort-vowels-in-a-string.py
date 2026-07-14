class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        sorted_vowels = sorted(c for c in s if c in vowels)

        res = list(s)
        j = 0
        for i, ch in enumerate(s):
            if ch in vowels:
                res[i] = sorted_vowels[j]
                j += 1
        
        return "".join(res)


        
            