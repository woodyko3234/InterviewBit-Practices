class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        n = len(A)
        if B not in A: return n
        else:
            end = 0
            for i in range(n):
                if A[i] != B:
                    A[end] = A[i]
                    end += 1
        return len(A[:end])
