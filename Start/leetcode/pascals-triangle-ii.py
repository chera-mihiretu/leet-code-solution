class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = 0
        pas = [[1]]
        while row < rowIndex:
            next_lin = []
            next_lin.append(1)
            for i in range(len(pas[-1])):
                if i + 1 < len(pas[-1]):
                    next_lin.append(pas[-1][i] + pas[-1][i+1])
                else:
                    next_lin.append(pas[-1][-1])
            pas.append(next_lin)
            row += 1

        return pas[-1]