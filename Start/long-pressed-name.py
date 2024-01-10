class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pointer = 0
        
        for i in range(len(name)):
            if pointer >= len(typed):
                return False
            if i == 0:
                if name[i] != typed[pointer]:
                    return False
            if name[i] == typed[pointer]:
                pointer += 1
            elif name[i] == name[i-1]:
                return False
            else:
                while typed[pointer] == name[i-1]:
                    pointer += 1
                    if pointer >= len(typed):
                        return False
                if name[i] == typed[pointer]:
                    pointer += 1
                else:
                    return False
        while pointer < len(typed):
            if typed[pointer] == typed[pointer-1]:
                pointer += 1
            else:
                return False
        return True
                