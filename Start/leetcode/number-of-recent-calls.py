class RecentCounter:

    def __init__(self):
        self.li = deque()

    def ping(self, t: int) -> int:
        self.li.append(t)

        while self.li[-1] - self.li[0] > 3000:
            self.li.popleft()
        return len(self.li)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)