class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        #brute force
        m = len(A)
        if m == 0: return []
        n = len(A[0])
        if n == 0: return A
        zero_col = set()
        zero_row = set()
        
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
        
        for i in zero_col:
            for j in range(m):
                A[j][i] = 0
                
        for i in zero_row:
            A[i] = [0] * n
            
        return A
