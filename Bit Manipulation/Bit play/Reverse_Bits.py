class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        reversedBin = bin(A)[:1:-1]
        output = 0
        for i in range(len(reversedBin)):
            output += int(reversedBin[i]) * (2**(31 - i))
        return output
