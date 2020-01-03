'''
sudoku: 
1. no duplicates in each row
2. no duplicates in each col
3. no duplicates in each block (3*3)
'''
#Do 3 checks together
from collections import defaultdict
class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        rows = len(A)
        cols = len(A[0])
        all_rows = dict()
        all_cols = dict()
        all_blocks = dict()
        for i in range(9):
            all_rows[i] = defaultdict(bool)
            all_cols[i] = defaultdict(bool)
            all_blocks[i] = defaultdict(bool)
            
        for row in range(rows):
            for col in range(cols):
                if A[row][col] == '.': pass
                elif all_blocks[(row//3) + (col//3)*3][A[row][col]] or all_rows[row][A[row][col]] or all_cols[col][A[row][col]]:
                    return 0
                else:
                    all_blocks[(row//3) + (col//3)*3][A[row][col]] = True
                    all_cols[col][A[row][col]] = True
                    all_rows[row][A[row][col]] = True
        return 1
