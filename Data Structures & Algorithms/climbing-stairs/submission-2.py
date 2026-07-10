class Solution:
    def climbStairs(self, n: int) -> int:
        past2 = 0
        past1 = 1

        for i in range(n):
            current = past1 + past2
            past2 = past1
            past1 = current

        return past1