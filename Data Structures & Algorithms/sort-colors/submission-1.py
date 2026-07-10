class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0, 0, 0]

        for i in range(len(nums)):
            counts[nums[i]] += 1

        idx = 0

        for i in range(len(nums)):
            while counts[idx] == 0:
                idx += 1
            
            nums[i] = idx
            counts[idx] -= 1

        return

