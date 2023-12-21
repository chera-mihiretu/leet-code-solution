class Solution(object):

    def romanToInt(self, s):
        self.key = {"I":1, "V": 5,"X":10, "L":50, "C":100, "D":500, "M":1000}
        x = 0
        for i in range(len(s)):
            if(i != 0):
                if( self.key[s[i]] > self.key[s[i-1]]):
                    x += self.key[s[i]] - self.key[s[i-1]]*2
                else:
                    x += self.key[s[i]]
            else:
                x += self.key[s[i]]
        return x
            
        