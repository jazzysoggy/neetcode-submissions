class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        left = ['{', '[', '(']
        right = ['}', ']', ')']

        for char in s:
            if char in left:
                stack.append(char)
            elif char in right:
                if len(stack) == 0:
                    return False

                if not (char == '}' and stack[-1] == '{') and not (char == ')' and stack[-1] == '(') and not (char == ']' and stack[-1] == '['):
                    return False
                
                stack.pop()

        return len(stack) == 0