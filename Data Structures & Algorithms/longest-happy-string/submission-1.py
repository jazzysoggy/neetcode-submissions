class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heapq.heappop(maxHeap)

            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break

                count2, char2 = heapq.heappop(maxHeap)

                res += char2
                if count2 + 1:
                    heapq.heappush(maxHeap, (count2 + 1, char2))
                
                heapq.heappush(maxHeap, (count, char))
                
            else:
                res += char
                if count + 1:
                    heapq.heappush(maxHeap, (count + 1, char))

        return res