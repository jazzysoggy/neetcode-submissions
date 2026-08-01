class Solution:
    def hammingWeight(self, n: int) -> int:
        bitCounts = 0

        while n > 0:
            bitCounts += n & 1

            n = n >> 1

        return bitCounts