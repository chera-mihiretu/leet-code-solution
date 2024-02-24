class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s:
            if i == '#':
                stack1 and stack1.pop()
            else:
                stack1.append(i)
        for i in t:
            if i == '#':
                stack2 and stack2.pop()
            else:
                stack2.append(i)
        if stack1 == stack2:
            return True
        else:
            return False
