class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        negativeArray = [nums[0]]
        positiveArray = [nums[0]]

        for i in range(1, len(nums)):
            num = nums[i]
            if num > 0:
                negativeArray.append(min(negativeArray[-1] * num, num))
                positiveArray.append(max(positiveArray[-1] * num, num))
            elif num < 0:
                negativeArray.append(min(positiveArray[-1] * num, num))
                positiveArray.append(max(negativeArray[-2] * num, num))
            else:
                positiveArray.append(0)
                negativeArray.append(0)

        return max(positiveArray)
