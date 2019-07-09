class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        ## O(n^2)
        n = len(A)
        maxv = 0
        i, j = 0, n-1
        while i < j:
            w = j - i
            h = min([A[i], A[j]])
            if w * h > maxv: maxv = w * h
            if A[i] > A[j]: j -= 1
            else: i += 1
        return maxv
