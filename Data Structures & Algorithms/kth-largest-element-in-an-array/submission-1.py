class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_output = []

        for num in nums:
            heapq.heappush(heap_output, num)

            if len(heap_output) > k:
                heapq.heappop(heap_output)

        return heap_output[0]

