from random import randint as rand
class RandomizedSet:

    def __init__(self):
        self.the_map = {}
        self.li = []
    def insert(self, val: int) -> bool:
        if val in self.the_map:
            return False
        else:
            self.the_map[val] = len(self.li)
            self.li.append(val)
            return True
    def remove(self, val: int) -> bool:
        if val in self.the_map:
            self.li[self.the_map[val]] = self.li[-1]
            self.the_map[self.li[-1]] = self.the_map[val]
            self.the_map.pop(val)
            self.li.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        value = self.li[rand(0, len(self.li)-1)]
        return value


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()