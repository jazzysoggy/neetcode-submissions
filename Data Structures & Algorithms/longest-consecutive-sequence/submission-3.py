class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = defaultdict(int)
        output = 0

        for i in nums:
            if c[i] == 0:
                c[i] = 1 + c[i - 1] + c[i + 1]
                c[i - c[i - 1]] = c[i]
                c[i + c[i + 1]] = c[i]
                output = max(output, c[i])

        return output