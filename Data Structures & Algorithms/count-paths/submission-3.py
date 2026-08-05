class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tracker = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            tracker[i][0] = 1
        for i in range(n):
            tracker[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                tracker[i][j] = tracker[i-1][j] + tracker[i][j-1]

        return tracker[-1][-1]