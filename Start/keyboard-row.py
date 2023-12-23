class Solution(object):
    def findWords(self, words):
        key = ["qwertyuiop", "asdfghjkl","zxcvbnm"]
        key_hash = {v:r for r in range(len(key)) for v in key[r]}
        row = None
        l = []
        
        for i in words:
            row = None
            can = None
            for j in i:
                if row == None:
                    row = key_hash[j.lower()]
                else:
                    if row != key_hash[j.lower()]:
                        break
            else:
                l.append(i)
        return l
        
                        
        