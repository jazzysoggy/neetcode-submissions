class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for i in range(n)]] * m
        paths[0][0] = 1

        for i in range(m):
            for j in range(n):
                left = paths[i-1][j] if i > 0 else 0
                top = paths[i][j-1] if j > 0 else 0
                paths[i][j] = max(paths[i][j], top + left)

        return paths[-1][-1]