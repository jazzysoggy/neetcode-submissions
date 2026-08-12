class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = []
        def backtrack(l_deficit, l_total):
            if l_total == n and l_deficit == 0:
                output.append("".join(stack))
                return

            if l_total < n:
                stack.append('(')
                backtrack(l_deficit + 1, l_total + 1)
                stack.pop()
                
            if l_deficit > 0:
                stack.append(')')
                backtrack(l_deficit - 1, l_total)
                stack.pop()


        backtrack(0,0)
        return output
