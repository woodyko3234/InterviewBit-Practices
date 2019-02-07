import copy
class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        #All elements in the array are in the range [0, N-1]
        a_len = len(A)
        if a_len <= 1: return A
        
        B = copy.deepcopy(A)
        
        for i in range(a_len):
            new_idx = A[i]
            A[i] = B[new_idx]
            
        return A
            
