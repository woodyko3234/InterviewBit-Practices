class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        byte = list(bin(A)[2:])
        byte = ([0] * (32 - len(byte))) + byte
        reverseVal = 0
        for i in range(31,-1,-1):
            if int(byte[i]) == 1:
                reverseVal += 2**(i)
        return reverseVal
