class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = defaultdict(int)
        output = 0
        for idx in nums:
            if track[idx] == 0:
                track[idx] = 1 + track[idx - 1] + track[idx + 1]

                track[idx - track[idx - 1]] = track[idx]
                track[idx + track[idx + 1]] = track[idx]
                output = max(output, track[idx])
        return output