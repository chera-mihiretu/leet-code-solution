class Solution:
    def freqAlphabets(self, s: str) -> str:
        a = 0
        b = 0
        ret_st = ""
        while a < len(s) or b < len(s):
            if b >= len(s):
                ret_st += chr(96+int(s[a]))
                a += 1
                continue
            if s[b] == '#':
                if (b -a) != 2:
                    ret_st += chr(96+int(s[a]))
                    a += 1
                    continue
                else:
                    ret_st += chr(96+int(s[a:b]))
                    b+=1
                    a = b
                    continue
            if s[b] != '#':
                b += 1
        return ret_st
