class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = set()

        for i in nums:
            if i in track:
                return True
            track.add(i)

        return False