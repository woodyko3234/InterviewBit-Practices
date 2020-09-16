class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)
        if n <= 1: return n
        higherL = [0] * n
        higherR = [0] * n
        candies = [1] * n
        for i in range(n):
            if i == 0:
                iLeft, iRight = i, i+1
            elif i == n-1:
                iLeft, iRight = i-1, i
            else:
                iLeft, iRight = i-1, i+1
            
            if A[i] > A[iLeft]:
                higherL[i] = 1
                candies[i] = candies[i-1] + 1
            if A[i] > A[iRight]:
                higherR[i] = 1
        for i in range(n-1, -1, -1):
            if higherR[i] == 1:
                if candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1] + 1
        return sum(candies)
