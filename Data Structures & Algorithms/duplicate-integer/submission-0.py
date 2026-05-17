class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}

        for i in nums:
            if i in dictionary:
                return True
            dictionary[i] = True
        
        return False