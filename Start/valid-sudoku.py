class Solution(object):
    def isValidSudoku(self, board):
        row_count = defaultdict(Counter)
        cols_count = defaultdict(Counter)
        box = defaultdict(Counter)
        
        for rows in range(9):
            for cols in range(9):
                if board[rows][cols] !=  ".":
                    row_count[rows][int(board[rows][cols])] +=1 
                    if row_count[rows][int(board[rows][cols])] > 1:
                        return False
                    cols_count[cols][int(board[rows][cols])] += 1
                    if cols_count[cols][int(board[rows][cols])] > 1:
                        return False
                    box[(rows//3, cols//3)][int(board[rows][cols])] += 1
                    if box[(rows//3, cols//3)][int(board[rows][cols])] > 1:
                        return False
                
        return True

        