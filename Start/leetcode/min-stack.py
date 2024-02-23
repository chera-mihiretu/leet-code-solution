class MinStack:

    def __init__(self):
        self.deq = deque()
        self.min = float('inf')
    def push(self, val: int) -> None:
        self.deq.append(val)        

    def pop(self) -> None:
        self.deq.pop()

    def top(self) -> int:
        return self.deq[-1]  

    def getMin(self) -> int:
        return min(self.deq)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()