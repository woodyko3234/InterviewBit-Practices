from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        n, output = len(A), []
        pairwiseSum = defaultdict(list)
        for i in range(n-1):
            for j in range(i+1, n):
                if len(pairwiseSum[A[i]+A[j]]) == 0: pass
                elif len(pairwiseSum[A[i]+A[j]]) >= 2: continue
                #restrictions: A1 < B1, C1 < D1
                #A1 < C1, B1 != D1, B1 != C1
                elif (i <= pairwiseSum[A[i]+A[j]][0][0]) or (
                    pairwiseSum[A[i]+A[j]][0][1] == i) or (
                    pairwiseSum[A[i]+A[j]][0][1] == j):
                    continue
                pairwiseSum[A[i]+A[j]].append([i, j])
        for val in pairwiseSum.values():
            if len(val) < 2: continue
            if not output: pass
            elif (val[0][0] < output[0]): pass
            elif (val[0][0] > output[0]): continue
            elif (val[0][1] < output[1]): pass
            elif (val[0][1] > output[1]): continue
            elif (val[1][0] < output[2]): pass
            elif (val[1][0] > output[2]): continue
            elif (val[1][1] < output[3]): pass
            elif (val[1][1] > output[3]): continue
            output = [val[0][0], val[0][1], val[1][0], val[1][1]]
        return output
