from collections import defaultdict
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        if len(A) <= 1: return -1
        output = defaultdict(int)
        for i in A:
            output[i] += 1
            if output[i] > 1: return i
        return -1
