class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        curr = 1

        for i in range(n):
            last = curr
            curr = curr + prev
            prev = last

        return curr
            