class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        zeros = [0] * 32
        ones = [0] * 32
        n = len(A)
        for i in range(n):
            cur = A[i]
            idx = 0
            while cur > 0 and idx < 32:
                if cur % 2 == 0: pass
                else:
                    ones[idx] += 1
                idx += 1
                cur = cur >> 1
        
        sum_diff = 0
        for i in range(32):
            zeros[i] = n - ones[i]
            sum_diff += 2*zeros[i]*ones[i]
        return sum_diff%(10**9+7)
