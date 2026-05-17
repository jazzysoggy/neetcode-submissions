class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = defaultdict(int)

        for i in nums:
            dictionary[i] += 1
            if dictionary[i] >= 2:
                return True

        return False