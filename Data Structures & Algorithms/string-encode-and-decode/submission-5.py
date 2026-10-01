class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        l = 0
        r = 1
        while l in range(len(s) - 1):
            
            while s[r] != "#":
                r += 1 
            result.append(s[r + 1 : r + 1 + int(s[l: r])])
            l = r + int(s[l: r]) + 1
            r = l + 1
        
        return result
