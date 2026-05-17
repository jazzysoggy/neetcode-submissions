class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0

        while n != 0:
            toAdd = n & 1
            output += toAdd
            n = n >> 1

        return output