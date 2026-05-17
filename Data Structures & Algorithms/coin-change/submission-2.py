class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        reachable = defaultdict(int)

        for coin in coins:
            reachable[coin] = 1

        for i in range(1, amount):
            if reachable[i] == 0:
                continue
            
            for coin in coins:
                if reachable[coin + i] == 0:
                    reachable[coin + i] = reachable[i] + 1
                else:
                    reachable[coin + i] = min(reachable[i] + 1, reachable[coin + i])

  
        return reachable[amount] if reachable[amount] != 0 else -1
