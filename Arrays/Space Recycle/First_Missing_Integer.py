class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        #Given an unsorted integer array, find the first missing positive integer.
        a_len = len(A)
        if a_len == 0: return 1
        
        #linear method
        idx_list = [i for i in range(1, a_len + 1)]
        #the missing value must be in the range of (1, len(A))
        for i in range(a_len):
            try:
                if A[i] > 0:
                    idx_list[A[i] - 1] = -1
            except: continue
        
        for idx in range(a_len):
            if idx_list[idx] != -1:
                return idx_list[idx]
        
        return a_len+1
