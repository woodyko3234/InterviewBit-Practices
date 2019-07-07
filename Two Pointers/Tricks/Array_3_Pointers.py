class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        i, j, k = 0, 0, 0
        m, n, o = len(A), len(B), len(C)
        min_max = None
        while i < m and j < n and k < o:
            cur_val = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
            if min_max is None or cur_val < min_max:
                min_max = cur_val
            if cur_val == abs(A[i] - B[j]):
                if A[i] > B[j]:
                    j += 1
                else:
                    i += 1
            elif cur_val == abs(B[j] - C[k]):
                if B[j] > C[k]:
                    k += 1
                else:
                    j += 1
            else:
                if C[k] > A[i]:
                    i += 1
                else:
                    k += 1
        return min_max
