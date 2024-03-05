class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            popped = []
            number = []
            done = False
            while stack and s[i] == ']':
                if not done and stack[-1] != '[':
                    popped.append(stack.pop())
                elif not done:
                    stack.pop()
                    done = True
                if done and  stack and stack[-1].isdecimal():
                    number.append(stack.pop())
                elif done:
                    break
                    

            if done:
                popped.reverse()
                number.reverse()
                stack.append("".join(popped)*int("".join(number)))
                    

            if s[i] != ']':
                stack.append(s[i])       
        return "".join(stack)         
            






                 