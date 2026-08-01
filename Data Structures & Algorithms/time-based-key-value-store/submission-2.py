class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.keyStore:
            return ""

        l = 0
        r = len(self.keyStore[key]) - 1

        res = ""

        while l <= r:
            m = (l + r) // 2

            value, time = self.keyStore[key][m]

            print(time, timestamp, value)
            
            if time > timestamp:
                r = m - 1
            elif time < timestamp:
                res = value
                l = m + 1
            else:
                return value

        return res