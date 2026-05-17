class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def visit(i, j):
            nonlocal grid
            nonlocal visited
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return

            if grid[i][j] == "0" or visited[i][j]:
                return

            visited[i][j] = True

            visit(i-1,j)
            visit(i+1,j)
            visit(i,j-1)
            visit(i,j+1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == "1":

                    visit(i, j)

                    count += 1

        

        return count

