class OrderedStream:

    def __init__(self, n: int):
        self.pointer = 0
        self.list = ["" for _ in range(n)]
        self.size = n
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey-1] = value
        to_return = []
        while self.pointer < self.size and self.list[self.pointer] != "" :
            to_return.append(self.list[self.pointer])
            self.pointer += 1
        return to_return
            
            


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)