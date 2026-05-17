class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = 1
        maxi = max(piles)
        res = maxi

        while mini <= maxi:
            mid = (mini + maxi) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(float(i) / mid)

            if hours <= h:
                res = mid
                maxi = mid - 1
            elif hours > h:
                mini = mid + 1


        return res

