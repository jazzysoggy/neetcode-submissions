class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mininum = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - mininum)
            mininum = min(mininum, prices[i])

        return maxProfit