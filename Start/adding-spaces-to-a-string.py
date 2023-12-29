class Solution:
    def addSpaces(self, s: str, spaces) -> str:
        li = []
        li.append(s[:spaces[0]])
        for i in range(len(spaces)-1):
            li.append(s[spaces[i]:spaces[i+1]])
        li.append(s[spaces[-1]:])
        return " ".join(li)