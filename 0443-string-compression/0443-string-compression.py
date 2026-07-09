class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                res.append(chars[i - 1])
                if count > 1:
                    res.extend(str(count))
                count = 1
        res.append(chars[-1])
        if count > 1:
            res.extend(str(count))

        for i in range(len(res)):
            chars[i] = res[i]
        return len(res)
