class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0

        while n != 0:
            toAdd = n % 2
            output += toAdd
            n //= 2

        return output