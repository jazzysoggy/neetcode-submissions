class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        validCombo = defaultdict(int)

        def backtrack(idx, summed):
            nonlocal coins
            nonlocal amount
            if idx >= len(coins):
                return 0

            if summed == amount:
                return 1
            
            if summed > amount:
                return 0

            total = 0

            if not (idx, amount - summed - coins[idx]) in validCombo:

                addOnWorks = backtrack(idx, summed + coins[idx])

                validCombo[(idx, amount - summed - coins[idx])] = addOnWorks

            total += validCombo[(idx, amount - summed - coins[idx])]

            if not (idx + 1, amount - summed) in validCombo:

                skipWorks = backtrack(idx + 1, summed)

                validCombo[(idx + 1, amount - summed)] = skipWorks

            total += validCombo[(idx + 1, amount - summed)]

            return total
        
        return backtrack(0, 0)