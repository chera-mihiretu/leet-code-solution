class Solution:
    def totalMoney(self, n: int) -> int:
        left = n%7
        times = n//7
        number = 1
        total = 0
        for i in range(1, times+1):
            total += 7/2*(2*number+(7-1))
            number += 1
        for i in range(number, left+number):
            total += i
        return int(total)


