class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lastVal = []

        for op in operations:
            if op == "+":
                lastVal.append(lastVal[-1] + lastVal[-2])
            elif op == "D":
                lastVal.append(2 * lastVal[-1])
            elif op == "C":
                lastVal.pop(-1)
            else:
                lastVal.append(int(op))


        return sum(lastVal)