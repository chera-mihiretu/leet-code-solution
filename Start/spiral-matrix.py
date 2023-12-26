class Solution:
    def spiralOrder(self, matrix):
        inc = True
        forw = True
        li = []
        i = 0
        j = 0
        while True:
            li.append(matrix[i][j])
            matrix[i][j] = '.'
            if forw:
                if inc:
                    if j+1 >= len(matrix[0]) or matrix[i][j+1] == ".":
                        if i+1 >= len(matrix):
                            return li
                        if matrix[i+1][j] == ".":
                            return li
                        forw = False
                        i+=1
                    else:
                        j+= 1
                else:
                    if j-1 < 0 or matrix[i][j-1] == ".":
                        if matrix[i-1][j] == ".":
                            return li
                        forw = False
                        inc = False
                        i-=1
                    else:
                        j-= 1
            else:
                if inc:
                    if i+1 >= len(matrix) or matrix[i+1][j] == ".":
                        
                        if matrix[i][j-1] == ".":
                            return li
                        forw = True
                        inc = False
                        j-=1
                    else:
                        i+= 1
                else:
                    if i-1 < 0 or matrix[i-1][j] == ".":
                        if j+1 >= len(matrix[0]):
                            return li
                        if matrix[i][j+1] == ".":
                            return li
                        forw = True
                        inc = True
                        j+=1
                    else:
                        i -= 1