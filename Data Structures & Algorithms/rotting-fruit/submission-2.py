class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutesTillAll = -1

        numNotRot = 0
        traverse = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                numNotRot += grid[i][j] == 1
                if grid[i][j] == 2:
                    traverse.append([i, j])
        movement = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        if (numNotRot == 0):
            return 0

        while len(traverse) > 0:
            for i in range(len(traverse)):
                curr = traverse[0]
                traverse.popleft()
                
                for move in movement:
                    nextSq = [curr[0] + move[0], curr[1] + move[1]]

                    if nextSq[0] < 0 or nextSq[1] < 0 or nextSq[0] >= len(grid) or nextSq[1] >= len(grid[0]):
                        continue

                    if grid[nextSq[0]][nextSq[1]] != 1:
                        continue

                    grid[nextSq[0]][nextSq[1]] = 2

                    traverse.append(nextSq)

                    numNotRot -= 1       


            minutesTillAll += 1


        return -1 if numNotRot != 0 else minutesTillAll

        