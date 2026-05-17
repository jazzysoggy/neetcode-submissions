class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCosts = [-1] * (len(cost) + 1)

        minCosts[0] = 0
        minCosts[1] = 0

        for i in range(len(cost)):
            if i + 1 < len(cost) + 1 and minCosts[i + 1] == -1:
                minCosts[i + 1] = minCosts[i] + cost[i]
            elif i + 1 < len(cost) + 1:
                minCosts[i + 1] = min(minCosts[i] + cost[i], minCosts[i + 1])
            if i + 2 < len(cost) + 1 and minCosts[i + 2] == -1:
                minCosts[i + 2] = minCosts[i] + cost[i]
            elif i + 2 < len(cost) + 1:
                minCosts[i + 2] = min(minCosts[i] + cost[i], minCosts[i + 2])
                
        return minCosts[-1]