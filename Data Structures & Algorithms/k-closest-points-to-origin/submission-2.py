class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            heapq.heappush(heap, (-point[0] ** 2 - point[1] ** 2,tuple(point)))
            
            if len(heap) > k:
                heapq.heappop(heap)



        return [list(i[1]) for i in heap]