class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxWind = deque()

        left = 0
        right = 0

        output = []

        while right < len(nums):
            while len(maxWind) > 0 and nums[right] > nums[maxWind[-1]]:
                maxWind.pop()

            maxWind.append(right)

            right += 1

            if right - left > k:
                if maxWind[0] == left:
                    maxWind.popleft()
                left += 1

            if right - left == k:
                output.append(nums[maxWind[0]])

        return output