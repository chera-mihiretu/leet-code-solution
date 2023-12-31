class Solution:
    def maxSum(self, grid):
        li = []
        for row in range(3,len(grid)+1):
            for col in range(3, len(grid[0])+1):
                su = 0
                for j in range(1,4, 2):
                    for i in range(1,4):
                        su += grid[row-j][col-i]
                su += grid[row-2][col-2]
                li.append(su)
        return max(li)
                
                