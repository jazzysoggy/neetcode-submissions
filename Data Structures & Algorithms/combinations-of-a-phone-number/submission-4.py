class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        stack = []

        if len(digits) == 0:
            return output

        char_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def backtrack(idx):
            nonlocal digits
            nonlocal stack
            nonlocal output
            nonlocal char_map

            if idx >= len(digits):
                output.append("".join(stack))
                return

            for char in char_map[digits[idx]]:
                stack.append(char)
                backtrack(idx + 1)
                stack.pop()

        backtrack(0)
        return output