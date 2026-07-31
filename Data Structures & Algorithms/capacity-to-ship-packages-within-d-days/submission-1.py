class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        output = -1

        while l <= r:
            m = (l + r) // 2
            print(l, m, r)

            dayTrack = 0
            held = 0

            for weight in weights:
                if held + weight <= m:
                    held += weight
                else:
                    held = weight
                    dayTrack += 1
                    if dayTrack >= days:
                        break

            if dayTrack >= days:
                l = m + 1
            else:
                r = m - 1
                output = m



        return output
                    