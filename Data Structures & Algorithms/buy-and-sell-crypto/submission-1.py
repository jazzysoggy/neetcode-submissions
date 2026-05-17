class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minium = prices[0]
        sol = 0
        for price in prices:
            sol = max(price - minium, sol)
            minium = min(price, minium)

        return sol