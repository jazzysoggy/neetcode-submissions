class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        events = defaultdict(int)

        for trip in trips:
            events[trip[2]] += trip[0]
            events[trip[1]] -= trip[0]

        allKeys = list(events.keys())

        allKeys.sort()

        for key in allKeys:
            capacity += events[key]
            if capacity < 0:
                return False

        return True