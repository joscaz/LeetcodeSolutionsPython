class MinStack:

    def __init__(self):
        self.stack = []
        self.helper = []
        self.min_elem = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_elem is not None:
            if val < self.min_elem:
                self.min_elem = val
                self.helper.append(val)
            else:
                self.helper.append(self.min_elem)
        else:
            self.min_elem = val
            self.helper.append(self.min_elem)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.helper.pop()
            if self.stack:
                self.min_elem = self.helper[-1]
        if not self.stack:
            self.min_elem = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_elem


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()