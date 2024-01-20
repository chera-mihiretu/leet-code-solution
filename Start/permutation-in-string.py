class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_content = Counter(s1)
        start = 0
        end = len(s1) -1
        s2_perm = Counter(s2[:len(s1)])
        while end < len(s2):
            if s1_content == s2_perm:
                return True
            
            s2_perm[s2[start]] -= 1
            if s2_perm[s2[start]] == 0:
                s2_perm.pop(s2[start])
            start += 1
            end +=1
            if end < len(s2):
                s2_perm[s2[end]] += 1
        
        return False