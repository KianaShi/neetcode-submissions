class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        result = 0
        b = 0
        for i in range(len(s)):
            c = s[i]
            if c in dic and dic[c] >= b:
                b = dic[c] + 1
            result = max(result, i + 1 - b)
            dic[c] = i
        return result

        