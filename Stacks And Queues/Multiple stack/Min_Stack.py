class MinStack:
    def __init__(self):
        self.stack = []
        self.minimums = []
    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        self.minimums.append(x)
        if len(self.minimums) >= 2 and x > self.minimums[-2]:
            self.minimums[-1] = self.minimums[-2]
    # @return nothing
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minimums.pop()
        else: return -1
    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1
    # @return an integer
    def getMin(self):
        if self.minimums:
            return self.minimums[-1]
        return -1
