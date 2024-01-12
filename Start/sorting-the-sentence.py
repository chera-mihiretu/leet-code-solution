class Solution:
    def sortSentence(self, s: str) -> str:
        se = set(['1','2','3','4','5','6','7','8','9','0'])
        li = s.split()
        li.sort(key = lambda x: x[-1])
        
        li = [i[:-1] for i in li]
        return " ".join(li)
        
        