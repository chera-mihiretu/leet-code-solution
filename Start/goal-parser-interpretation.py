class Solution:
    def interpret(self, command: str) -> str:
        stack = ""
        out = ""
        for i in command:
            if i == "(":
                stack = "("
            elif i == ")" and stack == "(":
                stack = ""
                out += "o"
            elif i == ")" and stack != "(":
                continue
            else:
                stack = ""
                out += i
        return out

