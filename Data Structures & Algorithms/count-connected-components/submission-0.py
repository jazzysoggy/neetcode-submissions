class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        componentCount = 0
        visited = defaultdict(bool)
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(idx):
            nonlocal visited
            nonlocal graph

            visited[idx] = True

            for i in graph[idx]:
                if visited[i]:
                    continue

                dfs(i)

        for i in range(n):
            if visited[i]:
                continue

            componentCount += 1

            dfs(i)

        return componentCount