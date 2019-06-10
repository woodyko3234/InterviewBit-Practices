class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        p, q = 0, 0
        for i in range(len(A)):
            p = q & (p ^ A[i]) 
            q = p | (q ^ A[i])
        return q
