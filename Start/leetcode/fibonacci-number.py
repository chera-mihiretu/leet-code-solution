class Solution:
    def fib(self, n: int, hash = {}) -> int:
        if n < 2: return n
        if n in hash:
            return hash[n]
        hash[n] = self.fib(n-1, hash)+self.fib(n-2, hash)
        return hash[n]
        