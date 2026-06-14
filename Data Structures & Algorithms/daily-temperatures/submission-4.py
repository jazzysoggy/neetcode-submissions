class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]
        tracking = [(temperatures[-1], len(temperatures) - 1)]

        for i in range(len(temperatures) - 2, -1, -1):
            while len(tracking) > 0 and temperatures[i] >= tracking[-1][0]:
                tracking.pop(-1)

            if len(tracking) > 0:
                output.append(tracking[-1][1] - i)
            else:
                output.append(0)

            tracking.append((temperatures[i], i))

        return list(reversed(output))