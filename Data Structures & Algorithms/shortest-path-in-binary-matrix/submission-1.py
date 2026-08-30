class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        distance = 0

        queue = deque()
        queue.append((0,0))

        if grid[0][0] == 1:
            return -1

        grid[0][0] = 1

        directions = [(1,0), (0,1), (1,1), (1,-1), (-1, 1), (-1, -1), (-1,0), (0,-1)]

        while len(queue) > 0:
            n = len(queue)

            for i in range(n):
                x,y = queue.popleft()

                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return distance + 1

                for x_delta, y_delta in directions:
                    new_x, new_y = x + x_delta, y + y_delta
                    
                    if new_x < 0 or new_y < 0:
                        continue

                    if new_x >= len(grid) or new_y >= len(grid):
                        continue

                    if grid[new_x][new_y] == 1:
                        continue

                    grid[new_x][new_y] = 1
                    queue.append((new_x, new_y))

            distance += 1

        return -1