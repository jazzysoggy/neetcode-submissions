class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        output = r

        while l <= r:
            m = (l + r) // 2
            time = sum([math.ceil(i / m) for i in piles])
            if time > h:
                l = m + 1
            elif time <= h:
                r = m - 1
                output = min(m, output)

        return output