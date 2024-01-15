class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        end = 0
        max_sub = 0
        max_ret = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while end < len(s) and max_sub < k:
            if end==0:
                if s[end] in vowels:
                    max_sub +=1
                    
            if end-start < k-1:
                if s[end+1] in vowels:
                    max_sub += 1
                    
                end += 1
            else:
                if s[start] in vowels:
                    max_sub -= 1
                if end+1 < len(s) and s[end+1] in vowels:
                    max_sub += 1
                
                start +=1
                end +=1
            max_ret = max(max_ret, max_sub)
        return max_ret
            
                
            