class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                curr = stack.pop()
                curr2 = stack.pop()

                stack.append(curr + curr2)
                
            elif i == "-":
                curr = stack.pop()
                curr2 = stack.pop()

                stack.append(curr2 - curr)
            elif i == "*":
                
                curr = stack.pop()
                curr2 = stack.pop()

                stack.append(curr2 * curr)
            elif i == "/":
                curr = stack.pop()
                curr2 = stack.pop()

                stack.append(int(curr2 / curr))
            else:
                stack.append(int(i))


        return stack[-1]