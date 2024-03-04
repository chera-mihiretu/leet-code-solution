class History:
    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage = History(homepage)
        self.pos = self.homepage
    def visit(self, url: str) -> None:
        self.pos.next = History(url, None, self.pos)
        self.pos = self.pos.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.pos.prev:
            self.pos = self.pos.prev
            steps -= 1
        return self.pos.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.pos.next:
            self.pos = self.pos.next
            steps -= 1
        return self.pos.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)