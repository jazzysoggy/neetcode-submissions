class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        queue = deque()

        l = 0
        r = 0

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            queue.append(r)
            
            while l > queue[0]:
                queue.popleft()
            

            if r + 1 >= k:
                output.append(nums[queue[0]])
                l += 1

            r += 1

        return output
