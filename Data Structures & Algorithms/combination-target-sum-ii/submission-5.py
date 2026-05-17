class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        stack = []

        nextItem = {}

        candidates = sorted(candidates)
        for i in range(len(candidates)):
            nextItem[candidates[i]] = i


        def backtrack(sumAll, idx):
            nonlocal output
            nonlocal stack
            nonlocal candidates
            nonlocal target
            nonlocal nextItem
            if sumAll == target and not stack in output:
                output.append(stack.copy())
                return
            if sumAll >= target or idx >= len(candidates):
                return

            stack.append(candidates[idx])
            backtrack(candidates[idx] + sumAll, idx + 1)
            stack.pop(-1)
            backtrack(sumAll, nextItem[candidates[idx]] + 1)

        backtrack(0, 0)
        
        return output