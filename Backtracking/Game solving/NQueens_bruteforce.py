class Solution:
    # @param n: integer
    # @return a list of list of strings
    def __init__(self):
        self.nQueens = []

    def puzzleChecker(self, puzzle, n):
        """Check whether there would be any other queen on their 
           moving paths
           There's no need to check horizontal or vertical
           since the situation is already considered when 
           defining puzzleMaker"""
        def quadrant1Checker(puzzle, row, col, n):
            if row > 0 and col < n-1:
                if puzzle[row-1][col+1] != "Q":
                    quadrant1Checker(puzzle, row-1, col+1, n)
                else: return False
            return True
            
        def quadrant2Checker(puzzle, row, col, n):
            if row > 0 and col > 0:
                if puzzle[row-1][col-1] != "Q":
                    quadrant2Checker(puzzle, row-1, col-1, n)
                else: return False
            return True
        
        def quadrant3Checker(puzzle, row, col, n):
            if row < n-1 and col > 0:
                if puzzle[row+1][col-1] != "Q":
                    quadrant3Checker(puzzle, row+1, col-1, n)
                else: return False
            return True
        
        def quadrant4Checker(puzzle, row, col, n):
            if row < n - 1 and col < n - 1:
                if puzzle[row+1][col+1] != "Q":
                    quadrant4Checker(puzzle, row+1, col+1, n)
                else: return False
            return True
        
        Q_col = []
        for i in range(n):
            Q_col.append(puzzle[i].find("Q"))
        for row, col in enumerate(Q_col):
            if not (quadrant1Checker(puzzle, row, col, n) and
                    quadrant2Checker(puzzle, row, col, n) and
                    quadrant3Checker(puzzle, row, col, n) and
                    quadrant4Checker(puzzle, row, col, n)):
                return False
        return True

    def solveNQueens(self, n):
        if n <= 3: return []
        def puzzleMaker(n, puzzle = [], row = 0, col = list(range(n))):
            puzzle = puzzle or []
            if len(puzzle) < row+1 and row < n:
                puzzle.append("."*n)
            elif row == n: 
                #print(puzzle)
                if self.puzzleChecker(puzzle, n):
                    self.nQueens += puzzle
                return
            for i in col:
                puzzle[row] = "."*i + "Q" + "."*(n-1-i)
                #print(puzzle)
                updated_col = col[:]
                updated_col.remove(i)
                puzzleMaker(n, puzzle, row+1, updated_col)
        puzzleMaker(n, [], 0, list(range(n)))
        #print(self.possiblePuzzles[:])
        #return self.possiblePuzzles
        return [self.nQueens[i*n:(i+1)*n] for i in range(len(self.nQueens)//n)]
