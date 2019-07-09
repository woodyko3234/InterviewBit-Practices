class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        n, m, l = len(A), len(B), len(C)
        i, j, k = 0,0,0
        min_max = float("inf")
        while i < n and j < m and k < l:
            comb = [A[i], B[j], C[k]]
            cur_min = min(comb)
            cur_diff = max(comb) - cur_min
            if cur_diff < min_max: min_max = cur_diff
            if A[i] == cur_min: i += 1
            elif B[j] == cur_min: j += 1
            else: k += 1
        return min_max
