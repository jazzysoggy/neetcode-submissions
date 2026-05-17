class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = 1
        maxi = max(piles)

        res = maxi

        while mini <= maxi:
            mid = (mini + maxi) // 2

            total = sum([math.ceil(i / mid) for i in piles])

            if total <= h:
                maxi = mid - 1
                res = mid
            elif total > h:
                mini = mid + 1

        return res
