class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()


        skip_list = defaultdict(int)

        for i in range(len(nums)):
            skip_list[nums[i]] = i

        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                summed = -nums[i] - nums[j]
                if summed in skip_list and skip_list[summed] > j:
                    triplets.append([nums[i], nums[j], nums[skip_list[summed]]])

                j = skip_list[nums[j]] + 1


            i = skip_list[nums[i]] + 1

        return triplets