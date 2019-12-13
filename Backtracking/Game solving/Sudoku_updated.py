class Solution:
    # @param A : list of list of chars
    # @return nothing
    def candidatorSettler(self, candidators, targetR, targetC, rows, cols, matrix):
        """
        To be a valid candidator, the item must be:
        1. Not duplicated in such row
        2. Not duplicated in such column
        3. Not duplicated in such matrix
        So it must be a number not shown in its row, col, and matrix.
        """
        for i in rows[targetR]:
            try:
                candidators.remove(i)
            except: continue
        for j in cols[targetC]:
            try:
                candidators.remove(j)
            except: continue
        for k in matrix[targetR//3 * 3 + targetC // 3]:
            try:
                candidators.remove(k)
            except: continue
        return candidators
    
    def candidatorsMaker(self, blanks, candLists, rows, cols, matrix): 
        """
        Find out the candidator lists which we can try fitting in
        but if the list only has one candidator, 
        we can just fill the blank without hesitation, then update
        the accompanied row, col, and matrix.
            
        If we cannot solve sudoku with just defined function candidatorsMaker,
        it would be necessary that we try to apply the candidators 
        and update the sudoku puzzle, to find out which combination works.
        """
        puzzle_unsolved = False
        for i in range(9):
            for j in blanks[i]:
                candLists[i][j] = self.candidatorSettler(candLists[i][j],i,j, 
                                                        rows, cols, matrix)
                if len(candLists[i][j]) == 1:
                    rows[i][j] = candLists[i][j][0]
                    cols[j][i] = candLists[i][j][0]
                    matrix[i//3 * 3 + j // 3].append(candLists[i][j][0])
                    blanks[i].remove(j)
                    #print(rows[0])
                    return (True, blanks, candLists, rows, cols, matrix)
        for i in range(9):
            if len(blanks[i]) == 0: continue
            #Try combinations to fix the puzzle
            puzzle_unsolved = True
            break
        if puzzle_unsolved: 
            rows = self.candidatorsTryer(rows)
                    
        return (False, blanks, candLists, rows, cols, matrix)

    def valChecker(self, trows, i, j, k):
        if (str(k) in trows[i]) or (str(k) in [trows[l][j] for l in range(9)]) \
            or (str(k) in [trows[i//3*3 + l][j//3*3] for l in range(3)]) \
            or (str(k) in [trows[i//3*3 + l][j//3*3 + 1] for l in range(3)]) \
            or (str(k) in [trows[i//3*3 + l][j//3*3 + 2] for l in range(3)]):
                return False
        return True

    def candidatorsTryer(self, rows, i = 0, j = 0):
        """
        After finding out that the sudoku puzzle cannot be finished with candidatorsMaker
        For the blanks left, we have to try each possible option 
        till one complete puzzle is done
        """
        if i == 9: return rows
        if j == 8:
            nextR = i+1
            nextC = 0
        else:
            nextR = i
            nextC = j + 1
        if rows[i][j] != "0": return self.candidatorsTryer(rows, nextR, nextC)
        for k in range(1, 10):
            if self.valChecker(rows, i, j, k):
                rows[i][j] = str(k)
                if self.candidatorsTryer(rows, nextR, nextC): return rows
                rows[i][j] = "0"
        return False
    
    def solveSudoku(self, A):
        """
        remember: we only need to try updating blanks with 
        possible candidators for that specific blank.
        if found any blanks with just one candidator,
        update the sudoku, break the loops, and re-run
        """
        rows = [['0' for _ in range(9)] for _ in range(9)]
        cols = [['0' for _ in range(9)] for _ in range(9)]
        matrix = [[] for _ in range(9)]
        blanks = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if A[i][j] != ".":
                    rows[i][j] = A[i][j]
                    cols[j][i] = A[i][j]
                    matrix[i//3 * 3 + j // 3].append(A[i][j])
                else:
                    blanks[i].append(j)
        #create candidators sets
        candLists = [[[] for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in blanks[i]:
                candLists[i][j] = list(map(str, range(1,10)))
        unsolved = True
        while unsolved:
            unsolved, blanks, candLists, rows, cols, matrix = self.candidatorsMaker(blanks, 
                                                                candLists, 
                                                                rows, cols, matrix)

        for i in range(9):
            A[i] = "".join(rows[i])
