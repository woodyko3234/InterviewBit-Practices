class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        return len("".join(bin(A)[2:].split("0")))
