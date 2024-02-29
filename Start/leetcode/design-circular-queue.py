class MyCircularQueue:

    def __init__(self, k: int):
        self.que = [-1] * k
        self.size = k
        self.cur_head = 0
        self.cur_tail = 0
        self.cur_size = 0

    def enQueue(self, value: int) -> bool:
        if self.cur_size < self.size:
            if self.que[self.cur_tail%self.size] != -1:
                self.cur_tail += 1
            self.que[self.cur_tail%self.size] = value
            self.cur_size +=1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.que[self.cur_head%self.size] != -1:
            self.que[self.cur_head%self.size] = -1
            if self.cur_head != self.cur_tail: 
                self.cur_head += 1
            self.cur_size -= 1
            return True
        else:
            return False
        

    def Front(self) -> int:
        return self.que[self.cur_head%self.size]

    def Rear(self) -> int:
        return self.que[self.cur_tail%self.size]

    def isEmpty(self) -> bool:
        return True if self.que[self.cur_head%self.size] == -1 else False

    def isFull(self) -> bool:
        return True if self.cur_size >= self.size else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()