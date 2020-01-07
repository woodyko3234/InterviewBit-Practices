class Solution:
    # @param A : tuple of integers
    # @param k : integer, non negative
    # @return an integer
    def diffPossible(self, A, k):
        """
        i can be greater or smaller than j
        so the condition can be modified as
        |A[i] - A[j]| = k
        """
        checklist, n = dict(), len(A)
        for i in range(n):
            if A[i] > k:
                try:
                    if checklist[A[i]]: return 1
                except:
                    checklist[A[i]-k] = i+1
            else:
                try:
                    if checklist[A[i]]: return 1
                except:
                    checklist[A[i]+k] = i+1
        return 0
