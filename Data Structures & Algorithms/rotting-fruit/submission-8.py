class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        equalBoard = deque()
        total = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    equalBoard.append((i,j))
                    total += 1
                    
                if grid[i][j] == 1:
                    total += 1

        timeLeft = -1

        if total == 0:
            return 0

        directs = [[1,0], [-1,0], [0,1], [0,-1]]

        while len(equalBoard) > 0:
            timeLeft += 1
            n = len(equalBoard)
            total -= n
            for i in range(n):
                i,j = equalBoard.popleft()
                

                for direct in directs:
                    x,y = i + direct[0], j + direct[1]

                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                        continue

                    if grid[x][y] != 1:
                        continue
                    
                    grid[x][y] = 2
                    equalBoard.append((x,y))

        return timeLeft if total == 0 else -1


