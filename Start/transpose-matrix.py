class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        mat = [[] for _ in range(len(matrix[0]))]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                mat[i].append(matrix[j][i])
        return mat
            