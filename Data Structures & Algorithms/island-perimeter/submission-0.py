class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                perimeter += i == 0 or grid[i - 1][j] == 0
                perimeter += i == len(grid) - 1 or grid[i + 1][j] == 0
                perimeter += j == 0 or grid[i][j - 1] == 0
                perimeter += j == len(grid[0]) - 1 or grid[i][j + 1] == 0

        return perimeter