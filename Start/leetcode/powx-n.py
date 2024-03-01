class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1

        if not n%2:
            val = pow(x, n//2)
            return val * val 
        else:
            val = pow(x, n//2) 
            return val * val * x

        