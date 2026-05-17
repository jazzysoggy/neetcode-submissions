class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        trackConsec = defaultdict(int)
        output = 0
        for num in nums:
            if trackConsec[num] != 0:
                continue
            trackConsec[num] = trackConsec[num - trackConsec[num - 1]] + trackConsec[num + trackConsec[num + 1]] + 1
            trackConsec[num - trackConsec[num - 1]] = trackConsec[num]
            trackConsec[num + trackConsec[num + 1]] = trackConsec[num]
            output = max(output, trackConsec[num])

        return output