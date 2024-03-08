class Solution:
    def mySqrt(self, x: int) -> int:
        start , end, best = 1, x, 1
        if x == 0:
            return 0
        while start <= end:
            mid = start + (end - start) // 2
            mul = (mid * mid)
            if  mul == x:
                return mid
            elif mul > x:
                end = mid - 1
            else:
                best = mid
                start = mid + 1
        
        return best