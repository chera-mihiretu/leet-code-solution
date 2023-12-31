class Bitset:
    def __init__(self, size: int):
        self.size =size
        self.bits = {1:{}, 0: {indx:0 for indx in range(size)}}
        self.bit_counts = 0

    def fix(self, idx: int) -> None:
        if idx not in self.bits[1]:
            self.bits[1][idx] = 0
            self.bits[0].pop(idx)
            self.bit_counts += 1


    def unfix(self, idx: int) -> None:
        if idx not in self.bits[0]:
            self.bits[0][idx] = 0
            self.bits[1].pop(idx)
            self.bit_counts -= 1

    def flip(self) -> None:
        
        zeros = self.bits.pop(0)
        ones = self.bits.pop(1)

        self.bits[1] =zeros
        self.bits[0] = ones

        self.bit_counts = abs(self.bit_counts - self.size)

    def all(self) -> bool:
        return self.bit_counts == self.size
   
    def one(self) -> bool:
        return self.bit_counts > 0

    def count(self) -> int:
        return self.bit_counts

    def toString(self) -> str:
        li = ["0" for _ in range(self.size)]
        for indx, val in self.bits[1].items():
            li[indx] = "1"
        return "".join(li)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()