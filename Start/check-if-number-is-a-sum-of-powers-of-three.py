class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        number = floor(pow(n,1/3))
        for i in range(number, -1,-1):
            if n == 0:
                return True
            if (n-pow(3,i))>=0:
                n=n-pow(3,i)
        if n == 0:
            return True
        return False
            