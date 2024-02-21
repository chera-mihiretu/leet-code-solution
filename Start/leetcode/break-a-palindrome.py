class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s = list(palindrome)
        for i in range(len(s)-1):
            if s[i] != 'a' and i != (len(s)//2):
                s[i] = 'a'
                return "".join(s)
        if s[-1] == 'a' and len(s) !=1:
            s[-1] = 'b'
            return "".join(s)
        elif len(s) != 1:
            s[-1] = 'a'
        return ""

        
