class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, board):
        self.solveSudokuRec(board,0,0)
    
    def solveSudokuRec(self, board,row,col):
        if row == 9:
            return True
        if col == 8:
            nextRow = row +1
            nextCol = 0
        else:
            nextRow = row
            nextCol = col+1
        if board[row][col]!='.':
            return self.solveSudokuRec(board,nextRow,nextCol)
        for c in range(1,10):
            if self.canPut(board,str(c),row,col):
                board[row][col] = str(c)
                if self.solveSudokuRec(board,nextRow,nextCol):
                    return True
                board[row][col] = '.'
        return False
    
    def canPut(self, board, char, row, col):
        for i in range(0,9):
            if board[row][i] == char:
                return False
            if board[i][col] == char:
                return False
        rowGroup = (row//3) * 3
        colGroup = (col//3) * 3 
        for i in range(rowGroup, rowGroup+3):
            for j in range(colGroup, colGroup+3):
                if board[i][j] == char:
                    return False
        return True
