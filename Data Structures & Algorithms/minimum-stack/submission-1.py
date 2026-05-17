class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.minStack) == 0 or val < self.stack[self.minStack[-1]]:
            self.minStack.append(len(self.stack))
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.minStack) != 0 and self.minStack[-1] == len(self.stack) - 1:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minStack[-1]]
