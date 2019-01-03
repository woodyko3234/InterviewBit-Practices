class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        N = len(A)
        if N == 1:
            return A 
        else:
            i = N-2
            while i >= 0 and A[i] >= A[i+1]:
                i -= 1
            if i == -1:
                return A[::-1]
            else:
                for j in range(N-1, i, -1):
                    if A[j] > A[i]:
                        break
                A[i], A[j] = A[j], A[i]
                a, b = i+1, N-1
                while a < b:
                    A[a], A[b] = A[b], A[a]
                    a += 1
                    b -= 1
            return A 
