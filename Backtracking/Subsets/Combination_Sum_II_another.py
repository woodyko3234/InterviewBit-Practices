class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    '''
    do not apply set to make elements unique
    [1,1,2,3], 5 => [[1,1,3],[2,3]]
    '''
    def combinationSum(self, A, B):
        A.sort()
        comb = []
        sumup = []
        self.recursion(A,B,sumup,comb)
        
        return comb
        
    def recursion(self, A, B, sumup, comb):
        if B < 0:
            return 
        elif B == 0 and sumup not in comb:
            comb.append(sumup)
            return 
        else:
            for i in range(len(A)):
                self.recursion(A[i+1:len(A)], B-A[i], sumup+[A[i]], comb)
