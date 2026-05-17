class Solution:
    def numSquares(self, n: int) -> int:
        previousSquares = [99999999999999] * (n + 1)

        previousSquares[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                previousSquares[i] = min(previousSquares[i], previousSquares[i - j * j] + 1)
                j += 1

        return previousSquares[-1]