class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        traverse = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    traverse.append([i, j])


        def handleTraverse(coord, dist):
            nonlocal grid
            nonlocal traverse

            if coord[0] < 0 or coord[1] < 0:
                return

            if coord[0] >= len(grid) or coord[1] >= len(grid[0]):
                return

            if grid[coord[0]][coord[1]] == -1:
                return

            if grid[coord[0]][coord[1]] != 2147483647:
                return

            grid[coord[0]][coord[1]] = dist + 1
            traverse.append(coord)

        moves = [[0,1], [0,-1], [1,0], [-1,0]]

        while len(traverse) > 0:
            curr = traverse[0]
            traverse.popleft()

            for move in moves:
                handleTraverse([curr[0] + move[0], curr[1] + move[1]], grid[curr[0]][curr[1]])
            