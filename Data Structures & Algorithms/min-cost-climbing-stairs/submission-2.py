class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [0] * len(cost)

        for i in range(2, len(cost)):
            minCost[i] = min(cost[i - 1] + minCost[i - 1], cost[i - 2] + minCost[i - 2])

        return min(minCost[-1] + cost[-1], minCost[-2] + cost[-2])
