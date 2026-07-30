class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = [0] * len(gas)

        tank[0] = gas[0]

        output = 0

        for i in range(1, len(gas)):
            tank[i] = tank[i - 1] - cost[i - 1]

            if tank[i] < 0:
                tank[i] = gas[i]
                output = i
            else:
                tank[i] += gas[i]

        return output

        

        

        