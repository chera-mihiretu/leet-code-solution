class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if i == ')':
                if stack[-1] == '(':
                    stack[-1] = 1
                    while len(stack) > 1:
                        if stack[-2] != '(':
                            stack[-2] = stack[-1] + stack[-2]
                            stack.pop()
                        else:
                            break
                else:
                    stack[-2] = stack[-1] * 2
                    stack.pop()
                    while len(stack) > 1:
                        if stack[-2] != '(':
                            stack[-2] = stack[-1] + stack[-2]
                            stack.pop()
                        else:
                            break
            else:
                stack.append(i)
        return stack[0]
                        
                        