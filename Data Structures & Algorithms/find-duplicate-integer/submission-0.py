class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        track = {}


        for num in nums:
            if not num in track:
                track[num] = True
            else:
                return num

        return -1