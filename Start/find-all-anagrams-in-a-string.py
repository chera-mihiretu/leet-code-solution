class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        container = Counter(s[:len(p)])
        start = 0
        end = len(p) -1
        indes = set()
        while end < len(s)-1:
            if container == count:
                indes.add(start)
            container[s[start]] -= 1
            container[s[end+1]] += 1
            
        
            
            start +=1 
            
            end += 1
        else:
            if container == count:
                indes.add(start)
        return list(indes)
                