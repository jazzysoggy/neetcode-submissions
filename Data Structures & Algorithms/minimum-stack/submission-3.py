class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []        

    def push(self, val: int) -> None:

        if len(self.minStack) == 0 or self.stack[self.minStack[-1]] > val:
            self.minStack.append(len(self.stack))

        self.stack.append(val)

    def pop(self) -> None:
        if self.minStack[-1] + 1 == len(self.stack):
            self.minStack.pop(-1)

        return self.stack.pop(-1)

        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minStack[-1]]
