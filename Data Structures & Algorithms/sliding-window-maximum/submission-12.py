class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()


        output = []
        for r in range(len(nums)):
            if len(window) > 0 and window[0] <= r - k:
                window.popleft()

            while len(window) > 0 and nums[r] >= nums[window[-1]]:
                window.pop()

            window.append(r)

            if r >= k - 1:
                output.append(nums[window[0]])

        return output