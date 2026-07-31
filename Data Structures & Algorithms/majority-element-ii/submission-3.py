class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        tracker = defaultdict(int)
        output = []

        for num in nums:
            tracker[num] += 1

            if tracker[num] == len(nums) // 3 + 1:
                output.append(num)


        return output

        