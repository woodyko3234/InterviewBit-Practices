class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        n = len(A)
        reds, whites, blues = 0, 0, 0
        for i in A:
            if i == 0: reds += 1
            elif i == 1: whites += 1
            else: blues += 1
        return [0] * reds + [1] * whites + [2] * blues
