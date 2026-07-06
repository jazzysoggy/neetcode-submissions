class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            bit = n & 1
            output += bit
            output = output << 1
            print(output)
            n = n >> 1

        return output // 2