class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}

        islands = 0

        def search(i,j):
            queue = deque()

            queue.append([i,j])
            
            while len(queue) != 0:
                current = queue.popleft()
                if grid[current[0]][current[1]] == "0" or (current[0],current[1]) in visited:
                    continue
                
                visited[(current[0], current[1])] = True

                if current[0] > 0:
                    queue.append([current[0] - 1, current[1]])
                if current[0] + 1 < len(grid):
                    queue.append([current[0] + 1, current[1]])
                if current[1] > 0:
                    queue.append([current[0], current[1] - 1])
                if current[1] + 1 < len(grid[0]):
                    queue.append([current[0], current[1]  + 1])


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    print(i,j)
                    search(i,j)
                    islands += 1




        return islands

