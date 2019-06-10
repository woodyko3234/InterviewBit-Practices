class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        bitOnes = "".join(bin(A)[2:].split('0'))
        return len(bitOnes)
