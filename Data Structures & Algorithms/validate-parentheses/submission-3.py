class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for c in s:
            if c == "}":
                if len(result) == 0:
                    return False
                last = result.pop()
                if last != "{":
                    return False
            elif c == "]":
                if len(result) == 0:
                    return False
                last = result.pop()
                if last != "[":
                    return False
            elif c == ")":
                if len(result) == 0:
                    return False
                last = result.pop()
                if last != "(":
                    return False
            else:
                result.append(c)
        return len(result) == 0