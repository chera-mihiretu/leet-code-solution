class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        answer = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                if stack == []:
                    answer += 1
                else:
                    stack.pop()
        answer += len(stack)
        return answer