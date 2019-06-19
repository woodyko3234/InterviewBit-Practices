class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        n, m = len(A), len(B)
        i, j = 0,0
        new_A = []
        while i < n and j < m:
            if A[i] <= B[j]:
                new_A.append(A[i])
                i += 1
            else:
                new_A.append(B[j])
                j += 1
        if i == n:
            print(" ".join(map(str, new_A + B[j:]))+" ")
        else:
            print(" ".join(map(str, new_A + A[i:]))+" ")
