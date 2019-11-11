class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        A.sort()
        allpos = set()
        subset = []
        self.recursive(A, subset, allpos)
        
        allpos = list(allpos)
        for i in range(len(allpos)):
            allpos[i] = list(allpos[i])
        allpos.sort()
        return allpos
        
    def recursive(self, A, subset, allpos):
        if A:
            for i in range(len(A)):
                self.recursive(A[i+1:len(A)], subset+[A[i]], allpos)
            allpos.add(tuple(subset))
            return
        else:
            allpos.add(tuple(subset))
            return
