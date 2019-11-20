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
        def quadrant1Checker(row, col, n, Q_pos):
            while row > 0 and col < n-1:
                if (row-1, col+1) in Q_pos: return False
                else:
                    row -= 1
                    col += 1
            return True
            
        def quadrant2Checker(row, col, n, Q_pos):
            while row > 0 and col > 0:
                if (row-1, col-1) in Q_pos: return False
                else: 
                    row -= 1
                    col -= 1
            return True
        
        def quadrant3Checker(row, col, n, Q_pos):
            while row < n-1 and col > 0:
                if (row+1, col-1) in Q_pos: return False
                else: 
                    row += 1
                    col -= 1
            return True
        
        def quadrant4Checker(row, col, n, Q_pos):
            while row < n-1 and col < n-1:
                if (row+1, col+1) in Q_pos: return False
                else: 
                    row += 1
                    col += 1
            return True
        
        Q_pos = [(row, col) for row, col in enumerate(puzzle)]
        for row, col in Q_pos:
            if not (quadrant1Checker(row, col, n, Q_pos) and
                    quadrant2Checker(row, col, n, Q_pos) and
                    quadrant3Checker(row, col, n, Q_pos) and
                    quadrant4Checker(row, col, n, Q_pos)):
                return False
        #print(absAdd, absDe)
        return True

    def solveNQueens(self, n):
        if n <= 3: return []
        def puzzleMaker(n, puzzle = [], row = 0, col = list(range(n))):
            puzzle = puzzle or []
            if len(puzzle) < row+1 and row < n:
                #puzzle.append("."*n)
                puzzle.append(0)
            elif row == n: 
                #print(puzzle)
                if self.puzzleChecker(puzzle, n):
                    temp = []
                    for i in range(n):
                        temp.append("."*puzzle[i] + "Q" + "."*(n-1-puzzle[i]))
                    self.nQueens.append(temp)
                return
            for i in col:
                #puzzle[row] = "."*i + "Q" + "."*(n-1-i)
                puzzle[row] = i
                #print(puzzle)
                updated_col = col[:]
                updated_col.remove(i)
                puzzleMaker(n, puzzle, row+1, updated_col)
        puzzleMaker(n, [], 0, list(range(n)))
        #print(self.possiblePuzzles[:])
        #return self.possiblePuzzles
        return self.nQueens
