class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_pos = deque()
        output = []

        l = 0
        for r in range(len(nums)):
            while len(max_pos) > 0 and nums[max_pos[-1]] < nums[r]:
                max_pos.pop()

            max_pos.append(r)

            l = max(0, r - k + 1)
            if max_pos[0] < l:
                max_pos.popleft()

            if r >= k - 1:
                output.append(nums[max_pos[0]])

        return output