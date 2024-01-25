class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        cols = len(matrix[0]) +1
        rows = len(matrix) +1
        
        self.prefix_sum = [[0]*cols for _ in range(rows)]
        
        for row in range(1, rows):
            for col in range(1, cols):
                self.prefix_sum[row][col] = matrix[row-1][col-1] + self.prefix_sum[row-1][col] + self.prefix_sum[row][col-1] - self.prefix_sum[row-1][col-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        answer = self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row2+1][col1] - self.prefix_sum[row1][col2+1] + self.prefix_sum[row1][col1]
        return answer


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)