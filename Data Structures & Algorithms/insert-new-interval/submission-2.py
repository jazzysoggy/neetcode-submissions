class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        heapq.heapify(intervals)

        heapq.heappush(intervals, newInterval)

        if len(intervals) == 0:
            return []

        output = []

        output.append(heapq.heappop(intervals))

        while len(intervals) > 0:
            new_val = heapq.heappop(intervals)

            if output[-1][-1] >= new_val[0]:
                output[-1][-1] = max(output[-1][-1], new_val[1])
            else:
                output.append(new_val)


        return output

        