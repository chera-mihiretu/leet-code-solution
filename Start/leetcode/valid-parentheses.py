class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {"(":")", "{":"}", "[":"]"}
        for i in range(len(s)):
            if s[i] in hash.keys():
                stack.append(s[i])
            else:
                if stack != [] and hash[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        if stack != []:
            return False
        return True 
            
        