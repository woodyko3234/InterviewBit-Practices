class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def calcPainters(self, A, mid):
        total = 0
        painters = 1
        for x in range(len(A)):
            total = total + A[x]
            if total > mid:
                painters = painters+1
                total = A[x]
        return painters
        
    def paint(self, k, t, C):
        s = sum(C)
        high = s
        low = max(C)
        while low < high:
            mid = int((high+low)/2)
            requiredPainters = Solution.calcPainters(self, C, mid)
            if requiredPainters <= k:
                high = mid
            else:
                low = mid+1
        return (low*t)%10000003
