class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs = []
                    dfs.append((i,j))
                    island += 1

                    while len(dfs) > 0:
                        x,y = dfs.pop()
                        grid[x][y] = "0"

                        if x > 0 and grid[x-1][y] == "1":
                            dfs.append((x - 1, y))
                            
                        if y > 0 and grid[x][y - 1] == "1":
                            dfs.append((x, y - 1))

                        if x < len(grid) - 1 and grid[x+1][y] == "1":
                            dfs.append((x + 1, y))

                        if y < len(grid[0]) - 1 and grid[x][y + 1] == "1":
                            dfs.append((x, y + 1))

        return island