class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        a_unique = list(set(sorted(A)))
        combination = []
        sumup = []
        self.recursion(a_unique, B, sumup, combination)
        return combination
                    
    def recursion(self, A, B, sumup, comb):
        if sum(sumup) > B:
            return 
        elif sum(sumup) == B:
            comb.append(sumup)
            return 
        else:
            for i in range(len(A)):
                self.recursion(A[i:len(A)], B, sumup+[A[i]], comb)
