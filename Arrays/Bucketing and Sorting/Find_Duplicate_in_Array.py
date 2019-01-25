from collections import defaultdict
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        if len(A) <= 1: return -1
        output = defaultdict(bool)
        for i in A:
            if output[i]: return i
            else: output[i] = True
        return -1
