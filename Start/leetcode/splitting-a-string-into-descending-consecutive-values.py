class Solution:
    def splitString(self, s: str) -> bool:
        s = list(s)
        def toInt(val):
            return int(''.join(val))
        def check(s, pre=None):
            print(pre, s)
            for i in range(1, len(s)): # the number substring must contain atleast one element
                if pre - toInt(s[:i]) == 1:
                    if i == len(s):
                        return True
                    if check(s[i:], toInt(s[:i])):
                        return True
                elif pre - toInt(s[:i]) < 1:
                    return False
            if pre-toInt(s) == 1:
                return True
            return False
        for i in range(1, len(s)):
            if check(s[i:], toInt(s[:i])):
                return True
        return False
            

            
            
                
                