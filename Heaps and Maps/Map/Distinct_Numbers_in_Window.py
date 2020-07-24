from collections import Counter
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        n = len(A)
        output = []
        if B > n: return output
        counter = Counter(A[:B])
        output.append(len(counter))
        for i in range(B, n):
            counter[A[i-B]] -= 1
            counter[A[i]] += 1
            if counter[A[i-B]] == 0:
                counter.pop(A[i-B])
            output.append(len(counter))
        return output
