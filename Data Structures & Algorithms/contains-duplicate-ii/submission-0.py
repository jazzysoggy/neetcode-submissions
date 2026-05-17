class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = defaultdict(bool)

        for r in range(len(nums)):
            if r - k > 0:
                window[nums[r - k - 1]] = False

            if window[nums[r]]:
                return True

            window[nums[r]] = True

        return False