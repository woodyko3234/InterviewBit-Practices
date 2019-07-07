class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        n, curr = len(A), 0
        for i in range(n):
            if A[i] != B:
                A[curr] = A[i]
                curr += 1
        A = A[:curr]
        return curr
