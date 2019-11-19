class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        elements = set(range(0,A))
        diagonals, antidiagonals = set(), set()
        final = []
        self.GenerateHelper(elements, diagonals, antidiagonals, [], -1, final, A)
        board_array = []
        self.toString(final, board_array, A)
        return board_array
        
    def GenerateHelper(self, elements, diagonals, antidiagonals, partial, row, result_set, n):
        if not elements:
            result_set.append(partial[:])
        for col in elements:
            if ((row + 1 + col) not in diagonals) and ((row+1 - col) not in antidiagonals):
                elements.discard(col)
                partial.append(col)
                diagonals.add(row+1+col)
                antidiagonals.add(row+1-col)
                self.GenerateHelper(elements, diagonals, antidiagonals, partial, row+1, result_set, n)
                antidiagonals.discard(row+1-col)
                diagonals.discard(row+1+col)
                partial.pop()
                elements.add(col)
                
    def toString(self, final, board_array, n):
        for board in final:
            row_list = [['.'] * n for _ in xrange(n)]
            for row, col in enumerate(board):
                row_list[row][col] = 'Q'
            board_array.append([''.join(row) for row in row_list])
