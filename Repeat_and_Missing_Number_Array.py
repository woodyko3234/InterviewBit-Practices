from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        a_len = len(A)
        A = Counter(A)
        output = [0] * 2
        for i in range(1, a_len+1):
            A[i] -= 1
            if A[i] == 0:
                A.pop(i)
            elif A[i] == 1:
                output[0] = i
            else:
                output[1] = i
        return output
