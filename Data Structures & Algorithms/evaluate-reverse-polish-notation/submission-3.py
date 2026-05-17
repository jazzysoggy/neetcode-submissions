class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackToEval = []


        for token in tokens:
            if token == '+':
                right = stackToEval.pop()
                left = stackToEval.pop()

                stackToEval.append(left + right)
            elif token == '-':
                right = stackToEval.pop()
                left = stackToEval.pop()

                stackToEval.append(left - right)
            elif token == '*':
                right = stackToEval.pop()
                left = stackToEval.pop()

                stackToEval.append(left * right)
            elif token == '/':
                right = stackToEval.pop()
                left = stackToEval.pop()

                stackToEval.append(int(left / right))
            else:
                stackToEval.append(int(token))
        return stackToEval[-1]