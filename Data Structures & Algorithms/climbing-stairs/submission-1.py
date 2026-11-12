class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            pre1 = 1
            pre2 = 2
            cur = 0
            for i in range(3, n + 1):
                cur = pre1 + pre2
                pre1 = pre2
                pre2 = cur
            return cur