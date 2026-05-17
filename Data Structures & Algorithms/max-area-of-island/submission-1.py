class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        area = 0

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def visit(i, j):
            nonlocal grid
            nonlocal visited
            nonlocal area

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return

            if visited[i][j] or grid[i][j] == 0:
                return

            visited[i][j] = True

            area += 1
            visit(i-1,j)
            visit(i+1,j)
            visit(i,j+1)
            visit(i,j-1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 1:
                    
                    visit(i, j)
                    maxArea = max(area, maxArea)
                    area = 0

        return maxArea