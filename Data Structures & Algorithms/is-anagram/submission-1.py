class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        for c in s:
            if c in countS:
                countS[c] += 1
            else:
                countS[c] = 1
        
        for q in t:
            if q in countS:
                countS[q] -= 1
            else:
                countS[q] = -1
        
        for value in countS.values():
            if value != 0:
                return False
        
        return True
        