class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            if n%4 != 0:
                return False
            n = n/4
        if n == 1:
            return True
        return False