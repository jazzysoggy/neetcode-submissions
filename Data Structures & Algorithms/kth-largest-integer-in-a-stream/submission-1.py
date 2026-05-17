class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stack = nums
        self.k = k

        heapq.heapify(self.stack)

        while len(self.stack) > self.k:
            heapq.heappop(self.stack)

    def add(self, val: int) -> int:
        heapq.heappush(self.stack, val)
        while len(self.stack) > self.k:
            heapq.heappop(self.stack)

        return self.stack[0]