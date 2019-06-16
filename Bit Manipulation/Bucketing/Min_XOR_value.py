class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        minXOR = float('inf')
        ##O(n^2) method
        #for i in range(len(A)-1):
        #    for j in range(i+1, len(A)):
        #        if A[i] ^ A[j] < minXOR:
        #            minXOR = A[i] ^ A[j]
        ##O(n logn) method
        A = sorted(A)
        for i in range(len(A) - 1):
            if A[i] ^ A[i+1] < minXOR:
                minXOR = A[i] ^ A[i+1]
        return minXOR
