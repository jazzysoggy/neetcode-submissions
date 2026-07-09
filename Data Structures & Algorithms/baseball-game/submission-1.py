class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        operations.reverse()

        while len(operations) > 0:
            top = operations.pop(-1)
            
            if top == "+":
                record.append(record[-1] + record[-2])
            elif top == "D":
                record.append(record[-1] * 2)
            elif top == "C":
                record.pop(-1)
            else:
                record.append(int(top))

        return sum(record)