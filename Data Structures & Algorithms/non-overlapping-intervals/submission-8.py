class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], x[1]))

        toAdd = [0 for i in range(len(intervals))]
        toAdd[0] = 1
        prevEnd = intervals[0][1]


        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                toAdd[i] = toAdd[i - 1]
                prevEnd = min(prevEnd, intervals[i][1])
                continue
                
            toAdd[i] = max(toAdd[i], toAdd[i - 1] + 1)

            prevEnd = intervals[i][1]

        return len(intervals) - max(toAdd)