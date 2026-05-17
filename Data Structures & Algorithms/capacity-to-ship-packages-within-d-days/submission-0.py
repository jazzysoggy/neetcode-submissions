class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        output = 99999999999

        while l <= r:
            m = (l + r) // 2

            summed = 0
            shipped = 1
            for i in weights:
                if summed + i > m:
                    shipped += 1
                    if shipped > days:
                        break
                    summed = i
                else:
                    summed += i

            if shipped > days:
                l = m + 1
            else:
                r = m - 1
                output = min(output, m)


        return output
                    