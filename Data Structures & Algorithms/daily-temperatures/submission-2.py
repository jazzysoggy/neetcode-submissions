class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        trackWarmer = [len(temperatures) - 1]

        output = [0]

        for i in range(len(temperatures) - 2, -1, -1):
            while len(trackWarmer) > 0 and temperatures[trackWarmer[-1]] <= temperatures[i]:
                trackWarmer.pop(-1)

            if len(trackWarmer) == 0:
                output.append(0)
            else:
                output.append(trackWarmer[-1] - i)

            trackWarmer.append(i)

        return list(reversed(output))