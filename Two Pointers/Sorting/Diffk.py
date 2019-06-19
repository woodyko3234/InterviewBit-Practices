class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        '''
        whenever B + A[j] = A[i], return True
        A is sorted, if 0 <= i < j <= n-1, then A[0] <= A[i] <= A[j] <= A[n-1]
        do we need to take care of B is positive or negative?
        if B < 0: find B + A[j] = A[i]
        elif B > 0: find B + A[i] = A[j]
        elif B == 0: find A[i] = A[j]
        '''
        n = len(A)
        if n == 0: return 0
        first = 0
        second = 1
        while first < (n-1) and second < n:
            #second must be greater than first
            if second <= first:
                second += 1
            elif B > 0:
                if B + A[first] > A[second]:
                    second += 1
                elif B + A[first] < A[second]:
                    first += 1
                else:
                    return 1
            elif B < 0:
                if B + A[second] > A[first]:
                    first += 1
                elif B + A[second] < A[first]:
                    second += 1
                else:
                    return 1
            else:
                if A[first] < A[second]:
                    first += 1
                else:
                    #in a sorted array, A[first] always <= A[second]
                    return 1
        return 0
