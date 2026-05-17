class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totals = []

        for i in range(len(gas)):
            totals.append(gas[i] - cost[i])

        if sum(totals) < 0:
            return -1

        begin = 0
        current = 0
        for i in range(len(totals) - 1):
            current += totals[i]
            if current < 0:
                begin = i + 1
                current = 0


        return begin