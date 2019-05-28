class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        a_bin = bin(int(A))[2:]
        if sum(int(i) for i in a_bin) == 1 and a_bin[-1] != '1':
            return 1
        else: return 0
