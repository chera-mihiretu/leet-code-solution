class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def ops(a , b, c):
            if c == '-':
                return str(int(int(a) - int(b)))
            elif c == '+':
                return str(int(int(a) + int(b)))
            elif c == '/':
                return str(int(int(a) / int(b)))
            elif c == '*': 
                return str(int(int(a) * int(b)))
        operations = {'/', '+', '*', '-'}
        for i in range(len(tokens)):
            c = tokens[i]
            if stack and tokens[i] in operations:
                b = stack.pop()
                a = stack.pop()
                c = ops(a,b,tokens[i])
            stack.append(c)
        return int(stack[0])