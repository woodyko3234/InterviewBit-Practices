class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        '''Implement binary search for particular row,
           then binary search for particular item in the row.'''
        rows = len(A)
        cols = len(A[0])
        if B > A[-1][-1] or B < A[0][0]: return 0
        low_r, high_r = 0, rows
        low_c, high_c = 0, cols
        while low_r < high_r:
            mid_r = (low_r+high_r) // 2
            if B >= A[mid_r][0] and B <= A[mid_r][cols-1]:
                pick_r = mid_r
                break
            elif B < A[mid_r][0]:
                high_r = mid_r
            else:
                low_r = mid_r + 1
        try:
            pick_r
            while low_c < high_c:
                mid_c = (low_c+high_c) // 2
                if B == A[pick_r][mid_c]:
                    return 1
                elif B > A[pick_r][mid_c]:
                    low_c = mid_c + 1
                else:
                    high_c = mid_c
        except: pass
        return 0
                
