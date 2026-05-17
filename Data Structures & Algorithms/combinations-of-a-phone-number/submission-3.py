class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if (len(digits) == 0):
            return []

        output = []
        stack = []
        convert = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j','k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        def backtrack(idx):
            nonlocal output
            nonlocal stack
            nonlocal convert
            nonlocal digits

            if idx >= len(digits):
                output.append("".join(stack))
                return

            for i in convert[digits[idx]]:
                stack.append(i)
                backtrack(idx+1)
                stack.pop(-1)

        backtrack(0)
        return output