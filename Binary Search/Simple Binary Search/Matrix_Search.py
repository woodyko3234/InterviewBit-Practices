class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        '''Implement binary search for particular row,
           then binary search for particular item in the row.'''
        
        rows = len(A)
        cols = len(A[0])
        if cols == 0 or rows == 0: return 0
        
        else:
            target_row = self.binarySearchRow(A, B, rows, cols)
            if target_row == -1: return 0
            else:
                return self.binarySearchCol(A, B, target_row, cols)
            
        
    
    def binarySearchRow(self, A, B, rows, cols):
        begin = 0
        end = rows - 1
        
        while begin <= end:
            mid = int((begin + end)/2)
            if B > A[mid][cols-1]:
                begin = mid + 1
            elif B < A[mid][cols-1]:
                if B < A[mid][0]:
                    end = mid - 1
                else:
                    return mid
            else:
                return mid
        return -1
        
    def binarySearchCol(self, A, B, target_row, cols):
        begin = 0
        end = cols - 1
        
        while begin <= end:
            mid = int((begin + end)/2)
            if B > A[target_row][mid]:
                begin = mid + 1
            elif B < A[target_row][mid]:
                end = mid - 1
            else:
                return 1
        return 0
