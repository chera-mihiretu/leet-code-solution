class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        max_len = 0
        for i in s:
            if len(i) > max_len:
                max_len = len(i)
        list_to_return = []
        for i in range(max_len):
            line = ""
            space = 0
            for string in s:
                if len(string) <= i:
                    space += 1
                else:
                    line += " " * space + string[i]
                    space = 0
            
            list_to_return.append(line)
        return list_to_return
        

        
                