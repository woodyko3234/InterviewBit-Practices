import copy
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        m = len(A)
        if m == 0: return A
        n = len(A[0])
        
        #simple way
        output = copy.deepcopy(A)
        cur_col = 0
        for i in range(m):
            cur_row = m-1
            for j in range(n):
                output[i][j] = A[cur_row][cur_col]
                cur_row -= 1
            cur_col += 1
        
        return output
