class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        reachable = [-1] * (amount + 1)

        reachable[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    continue
                
                if reachable[i - coin] == -1:
                    continue
                
                if reachable[i] == -1:
                    reachable[i] = reachable[i - coin] + 1
                else:
                    reachable[i] = min(reachable[i], reachable[i - coin] + 1)

        print(reachable)
        return reachable[-1]
