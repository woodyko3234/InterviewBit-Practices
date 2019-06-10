class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        target = 0
        for i in range(len(A)):
            target = target ^ A[i]
        return target
