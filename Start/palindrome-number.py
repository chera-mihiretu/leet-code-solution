class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = list(str(x))
        y.reverse()
        y = int("".join(y))
        if x - y == 0:
            return True
        else:
            return False