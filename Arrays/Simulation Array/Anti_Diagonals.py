class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        output = []
        a_len = len(A)
        if a_len == 0: return output
        for i in range(1, 2*(len(A))):
            output.append([])
        
        rows = len(output)
        base_line = 0
        
        while base_line < a_len:
            row_idx = 0
            col_idx = base_line
            while col_idx >= 0:
                output[base_line].append(A[row_idx][col_idx])
                row_idx += 1
                col_idx -= 1
            base_line += 1
        while base_line < rows:
            row_idx = (base_line % a_len) + 1
            col_idx = a_len-1
            while row_idx < a_len:
                output[base_line].append(A[row_idx][col_idx])
                row_idx += 1
                col_idx -= 1
            base_line += 1
        return output
