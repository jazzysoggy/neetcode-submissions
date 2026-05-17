class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        createGraph = defaultdict(list)

        for edge in edges:
            createGraph[edge[0]].append(edge[1])
            createGraph[edge[1]].append(edge[0])

        visited = set()

        queue = deque()

        queue.append((0, -1))

        while len(queue) > 0:
            current = queue[0]
            queue.popleft()
            
            if current[0] in visited:
                return False

            visited.add(current[0])

            for node in createGraph[current[0]]:
                if node == current[1]:
                    continue
                
                queue.append((node, current[0]))

        return len(visited) == n