class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        su = 0
        if len(mat) == 1:
            return mat[0][0]
        for i in range(len(mat)):
            su += mat[i][i]
            if i == len(mat)//2 and len(mat) % 2:
                continue
            su += mat[len(mat)-i-1][i]
        return su