class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        m = len(A)
        n = len(B)
        if m == 0: return B
        elif n == 0: return A
        
        i, j = 0, 0 # idx in A and B
        C = []
        while i < m and j < n:
            if A[i] > B[j]:
                C.append(B[j])
                j += 1
            else: 
                C.append(A[i])
                i += 1
        if j < n:
            C = C + B[j:]
        elif i < m:
            C = C + A[i:]
        return C
