class Solution:
    # @param A : tuple of integers, filling gas
    # @param B : tuple of integers, consuming gas
    # @return an integer
    def canCompleteCircuit(self, A, B):
        #qualified starting points
        qS, C = [], []
        n = len(A)
        for i in range(n):
            C.append(A[i] - B[i])
            if A[i] - B[i] >= 0:
                qS.append(i)
        if sum(C) < 0: return -1 #definitely cannot finish
        for i in qS:
            route = C[i]
            j = (i+1) % n
            while j != i:
                route += C[j]
                if route < 0: break
                j += 1
            if route >= 0: return i
        return -1
