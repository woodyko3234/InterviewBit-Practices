class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        #input: index of the Pascal’s triangle
        if A == 0: return [1]
        elif A == 1: return [1,1]
        #how to do without referring to prior rows in the triangle?
        pre_row = [1,1]
        row = 2
        while row < A:
            row_lst = [1] * (row+1)
            to_push = 1
            to_end = row - 1
            while to_push <= to_end:
                row_lst[to_push] = pre_row[to_push-1] + pre_row[to_push]
                row_lst[to_end] = row_lst[to_push]
                to_push += 1
                to_end -= 1
            pre_row = row_lst
            row += 1
        
        output = [1] * (A+1)
        to_push = 1
        to_end = A - 1
        while to_push <= to_end:
            output[to_push] = pre_row[to_push-1]+pre_row[to_push]
            output[to_end] = output[to_push]
            to_push += 1
            to_end -= 1
        return output
        
            
        
