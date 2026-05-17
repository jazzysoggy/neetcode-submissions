class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        trackMinPrice = 99999999999
        profit = 0


        for price in prices:
            profit = max(profit, price - trackMinPrice)
            trackMinPrice = min(price, trackMinPrice)

        return profit