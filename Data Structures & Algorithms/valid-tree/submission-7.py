class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = {}

        dfs = [0]

        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited[0] = 0

        while len(dfs) > 0:
            curr = dfs.pop()

            for i in graph[curr]:
                if visited[curr] == i:
                    continue

                dfs.append(i)

                if i in visited:
                    return False

                visited[i] = curr


        return len(visited) == n
