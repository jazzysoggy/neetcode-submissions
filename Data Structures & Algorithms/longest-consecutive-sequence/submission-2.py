class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutives = defaultdict(int)

        length = 0

        for num in nums:
            if consecutives[num] == 0:
                consecutives[num] = 1 + consecutives[num - 1] + consecutives[num + 1]
                consecutives[num - consecutives[num - 1]] = consecutives[num]
                consecutives[num + consecutives[num + 1]] = consecutives[num]
                length = max(length, consecutives[num])
            
        return length