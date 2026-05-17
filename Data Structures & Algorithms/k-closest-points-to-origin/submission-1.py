class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []

        for point in points:
            heapq.heappush(output, (-(point[0] * point[0] + point[1] * point[1]), point))
            if len(output) > k:
                heapq.heappop(output)
        output = [i[1] for i in output]

        return output
