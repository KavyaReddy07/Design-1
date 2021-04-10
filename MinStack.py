class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if self.min < val:
            self.stack.append(val)
        else:
            self.stack.append(self.min)
            self.stack.append(val)
            self.min = val
                
    def pop(self) -> None:
        if not self.stack:
            return None
        curr = self.stack.pop(-1)
        if self.min == curr:
            self.min = self.stack.pop(-1)
        return curr
    
    
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()