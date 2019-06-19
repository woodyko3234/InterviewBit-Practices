class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n <= 2: return n
    
        end = 1
        for i in range(2, n):
            if A[i] == A[end-1]: pass
            else:
                A[end+1] = A[i]
                end += 1
        A = A[:end+1]
        return end+1
