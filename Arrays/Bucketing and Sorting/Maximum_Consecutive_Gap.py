class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) < 2: return 0
        #brute force method
        a_sort = sorted(list(A))
        max_diff = 0
        for i in range(len(a_sort)-1):
            max_diff = max(max_diff, a_sort[i+1]-a_sort[i])
        return max_diff
