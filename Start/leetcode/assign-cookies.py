class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        coc = 0
        if not s:
            return 0
        for i in range(len(g)):
            if g[i] <= s[coc]:
                g[i] = 0
                coc += 1
            else:
                while coc < len(s) and g[i] > s[coc]:
                    coc += 1
                if g[i] <= s[coc-1]:
                    g[i] = 0 
                coc +=1 

            if coc >= len(s) and g[i] == 0:
                return i+1
            elif coc >= len(s):
                return i
        return len(g)

