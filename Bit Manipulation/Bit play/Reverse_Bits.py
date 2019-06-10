class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        reverse = [0] * 32
        reversedBin = bin(A)[:1:-1]
        output = 0
        for i in range(len(reversedBin)):
            reverse[i] = int(reversedBin[i])
            output += reverse[i] * (2**(31 - i))
        return output
