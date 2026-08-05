class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        if len(self.low) == 0 and len(self.high) == 0:
            heapq.heappush(self.high, num)
            return

        if (len(self.high) + len(self.low)) % 2 == 0:
            if num < -self.low[0]:
                heapq.heappush(self.low, -num)
                heapq.heappush(self.high, -heapq.heappop(self.low))
            else:
                heapq.heappush(self.high, num)
        else:
            if num > self.high[0]:
                heapq.heappush(self.low, -heapq.heappop(self.high))
                heapq.heappush(self.high, num)
            else:
                heapq.heappush(self.low, -num)
        
        

    def findMedian(self) -> float:
        if (len(self.high) + len(self.low)) % 2 == 0:
            return (-self.low[0] + self.high[0]) / 2

        return self.high[0]
        