class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0

        for i in nums:
            current = max(i + rob2, rob1)
            rob2 = rob1
            rob1 = current

        return max(rob2, rob1)
