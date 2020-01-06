from collections import defaultdict
class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        '''
        To be valid, a sudoku puzzle must apply to:
        1. No duplicated int in the same row;
        2. No duplicated int in the same column; and
        3. No duplicated int in the same matrix
        The code doesn't have to check either the character("0") or the
        format("....8..79.") is valid or not.
        '''
        rows = defaultdict(dict)
        columns = defaultdict(dict)
        matrixes = defaultdict(dict)
        for i in range(9):
            rows[i] = dict()
            for j in range(9):
                if A[i][j] == ".": continue
                try:
                    if rows[i][A[i][j]]: return 0
                except:
                    rows[i][A[i][j]] = True
                if not columns[j]:
                    columns[j] = dict()
                try:
                    if columns[j][A[i][j]]: return 0
                except:
                    columns[j][A[i][j]] = True
                if not matrixes[i//3*3+j//3]:
                    matrixes[i//3*3+j//3] = dict()
                try:
                    if matrixes[i//3*3+j//3][A[i][j]]: return 0
                except:
                    matrixes[i//3*3+j//3][A[i][j]] = True
        return 1
