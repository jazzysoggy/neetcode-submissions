class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        uniquePaths = [0] * (n)
        uniquePaths[0] = 1

        for i in range(m):
            for j in range(1, n):
                uniquePaths[j] = uniquePaths[j - 1] + uniquePaths[j]


        return uniquePaths[-1]