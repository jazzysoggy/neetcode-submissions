class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodesAccessed = set()

        queue = []

        graph = defaultdict(list)

        for ui, vi, ti in times:
            graph[ui].append((vi, ti))

        queue.append((0, k))

        while len(queue) > 0:
            moment, node = heapq.heappop(queue)

            if node in nodesAccessed:
                continue

            nodesAccessed.add(node)

            if len(nodesAccessed) == n:
                return moment

            for target, lag in graph[node]:
                heapq.heappush(queue, (moment + lag, target))

        return -1