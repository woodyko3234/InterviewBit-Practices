class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        #brute force
        n = len(A)
        if n <= 1: return 0
        elif n == 2: return min(A)
    
        i = 0
        j = n-1
        maxArea = 0
        while i < j:
            maxArea = max(maxArea, (j-i)*min(A[i], A[j]))
            if A[i] < A[j]:
                i += 1
            else:
                j -= 1
        return maxArea
