class TimeMap:

    def __init__(self):
        self.timetrack = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.timetrack[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        toPush = []
        output = ""

        while len(self.timetrack[key]) > 0:
            time, value = heapq.heappop(self.timetrack[key])

            toPush.append((time, value))

            if time > timestamp:
                break

            output = value

        for item in toPush:
            heapq.heappush(self.timetrack[key], item)

        return output
        
