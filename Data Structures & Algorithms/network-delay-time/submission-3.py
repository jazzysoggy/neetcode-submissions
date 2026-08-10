class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        delayTime = 0

        if n <= 1:
            return delayTime

        graph = defaultdict(list)

        for time in times:
            graph[time[0]].append((time[1], time[2]))

        visited = defaultdict(bool)

        traverse = []

        heapq.heappush(traverse, (0,k))

        while len(traverse) > 0:
            time, node = heapq.heappop(traverse)

            if node in visited:
                continue

            delayTime = max(delayTime, time)

            visited[node] = True

            for target, time_add in graph[node]:
                heapq.heappush(traverse, (time + time_add, target))


        return delayTime if n == len(visited) else -1