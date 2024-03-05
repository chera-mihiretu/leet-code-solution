class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def search(row, col,  index):
            if index == len(word):
                return True
            if not (0 <= col < len(board[0]) and 0 <= row < len(board)):
                return False
            if board[row][col] != word[index]:
                return False
            board[row][col] = ''
            if search(row+1, col, index + 1):
                return True
            if search(row-1, col, index + 1):
                return  True

            if search(row, col+1, index + 1):
                return True
            if search(row, col-1, index + 1):
                return True
            board[row][col] = word[index]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if search(row,col, 0):
                        return True
                
            

