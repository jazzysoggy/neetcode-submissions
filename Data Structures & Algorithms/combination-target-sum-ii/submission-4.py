class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        stack = []

        candidates = sorted(candidates)

        def backtrack(sumAll, idx):
            nonlocal output
            nonlocal stack
            nonlocal candidates
            nonlocal target
            if sumAll == target and not stack in output:
                output.append(stack.copy())
                return
            if sumAll >= target or idx >= len(candidates):
                return

            stack.append(candidates[idx])
            backtrack(candidates[idx] + sumAll, idx + 1)
            stack.pop(-1)
            backtrack(sumAll, idx + 1)

        backtrack(0, 0)
        
        return output