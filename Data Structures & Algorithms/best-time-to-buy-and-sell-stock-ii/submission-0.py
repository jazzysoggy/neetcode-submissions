class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0] * len(prices)
        sell = [0] * len(prices)

        buy[0] = -prices[0]

        maxProfitToday = 0

        for i in range(1, len(prices)):
            price = prices[i]

            buy[i] = max(sell[i - 1] - price, buy[i-1])

            sell[i] = max(buy[i - 1] + price, sell[i-1])

            maxProfitToday = max(maxProfitToday, sell[i])

        print(buy)
        print(sell)

        return maxProfitToday