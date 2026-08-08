class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        stack = [0] * 26

        for task in tasks:
            stack[ord(task) - ord('A')] += 1

        stack.sort(reverse=True)

        idle = n * (stack[0] - 1)

        # X $ $ X 

        maxf = stack[0]

        for i in range(1, len(stack)):
            idle -= min(stack[i], maxf - 1)


        return max(idle, 0) + len(tasks)