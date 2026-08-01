class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        levelTraversal = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    levelTraversal.append((i,j))

        dist = 0
        direction = [[1,0], [0,1], [-1,0], [0,-1]]

        while len(levelTraversal) > 0:
            n = len(levelTraversal)

            for _ in range(n):
                x,y = levelTraversal.popleft()

                grid[x][y] = dist

                for direct in direction:
                    x_new, y_new = x + direct[0], y + direct[1]
                    if x_new >=0 and y_new >= 0 and x_new < len(grid) and y_new < len(grid[0]) and grid[x_new][y_new] == 2147483647:
                        levelTraversal.append((x_new, y_new))
                        grid[x_new][y_new] = -1

            dist += 1

        return