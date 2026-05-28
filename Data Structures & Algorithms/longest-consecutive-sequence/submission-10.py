class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        trackConsec = defaultdict(int)
        output = 0

        for num in nums:
            prev = num - 1
            post = num + 1
            if trackConsec[num] != 0:
                continue

            trackConsec[num] = trackConsec[prev] + trackConsec[post] + 1
            trackConsec[num - trackConsec[prev]] = trackConsec[num]
            trackConsec[num + trackConsec[post]] = trackConsec[num]
            output = max(output, trackConsec[num])

        print(trackConsec)
        return output
