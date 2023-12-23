class Solution:
    def numberOfMatches(self, n: int) -> int:
        match = 0
        while n > 1:
            if not n % 2:
                n = n//2 
                match += n
            else:
                match += (n-1)//2
                n = ((n-1)//2)+1
        return match