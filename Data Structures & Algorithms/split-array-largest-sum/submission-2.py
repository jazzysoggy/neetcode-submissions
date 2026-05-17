class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = min(nums)
        r = sum(nums)

        output = 999999999999

        while l <= r:
            m = (r + l) // 2

            maxSplit = 0

            splitCount = 1

            summed = 0

            for i in nums:
                if summed + i > m:
                    if splitCount == k:
                        splitCount += 1
                        break
                    else:
                        splitCount += 1
                        maxSplit = max(maxSplit, summed)
                        summed = i
                else:
                    summed = summed + i

            maxSplit = max(maxSplit, summed)

            if splitCount <= k:
                output = min(output, maxSplit)
                r = m - 1
            else:
                l = m + 1

        return output