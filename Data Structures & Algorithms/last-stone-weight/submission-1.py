class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stack = [-i for i in stones]

        heapq.heapify(stack)

        while len(stack) > 1:
            one = stack[0]
            heapq.heappop(stack)
            two = stack[0]
            heapq.heappop(stack)

            if one != two:
                heapq.heappush(stack, -abs(one - two))
        
        return -stack[0] if len(stack) == 1 else 0
        