class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        to_update = 0
        for i in range(1, n):
            if A[i] == A[to_update]: continue
            else:
                A[to_update+1] = A[i]
                to_update += 1
        A = A[:to_update+1]
        return len(A)
