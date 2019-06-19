class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        m, n = len(A), len(B)
        if m == 0 or n == 0: return []
        else:
            i = 0
            j = 0
            commons = []
            while i < m and j < n:
                if A[i] == B[j]:
                    commons.append(A[i])
                    i += 1
                    j += 1
                elif A[i] > B[j]:
                    j += 1
                else:
                    i += 1
            return commons
