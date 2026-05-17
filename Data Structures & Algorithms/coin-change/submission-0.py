class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinTrack = [-1] * (amount + 1)

        coinTrack[0] = 0

        for i in range(len(coinTrack)):
            for j in coins:
                if i - j >= 0 and coinTrack[i - j] != -1:
                    coinTrack[i] = min(coinTrack[i], coinTrack[i - j] + 1) if coinTrack[i] != -1 else coinTrack[i-j] + 1

        return coinTrack[amount]

