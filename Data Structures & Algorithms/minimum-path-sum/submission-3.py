class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        output = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        output[0][0] = grid[0][0]

        for i in range(1, len(grid)):
            output[i][0] = output[i - 1][0] + grid[i][0]

        for j in range(1, len(grid[0])):
            output[0][j] = output[0][j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                output[i][j] = grid[i][j] + min(output[i - 1][j], output[i][j - 1])

        return output[-1][-1]