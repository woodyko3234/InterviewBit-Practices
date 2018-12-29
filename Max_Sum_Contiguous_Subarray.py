class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        ans = 0
        sumup = 0
        a_len = len(A)
        for i in range(a_len):
            if sumup + A[i] > 0:
                sumup += A[i]
            else:
                sumup = 0
            ans = max(ans, sumup)
        if ans == 0: return max(A)
        else: return ans
