class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        n = len(A)
        binary_list = [bin(i)[2:] for i in A]
        max_len = max(len(i) for i in binary_list)
        bin_0 = [0] * max_len
        bin_1 = [0] * max_len
        sumup = 0
        for i in range(n):
            x = binary_list[i].zfill(max_len)
            for j in range(max_len):
                if x[j] == "0":
                    bin_0[j] += 1
                else:
                    bin_1[j] += 1
                if i == n-1:
                    sumup += bin_0[j] * bin_1[j]
        return (sumup * 2) % (10**9 + 7)
