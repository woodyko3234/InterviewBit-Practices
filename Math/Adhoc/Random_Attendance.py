class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        for i in B:
            ans.append(self.numk(A, i))
        return ans
        
    def numk(self, A, k):
        c = 1 #start from 1
        k -=1 #zero-based
        while k>0:
            step = self.get_steps(A, c)
            if step <= k:
                c+=1
                k-=step
            else:
                c*=10
                k-=1
        return c
        
    def get_steps(self, A, c):
        step = 0
        c1 = c
        c2 = c+1
        while c1 <= A:
            step += min(A+1, c2) - c1
            c1 *=10
            c2 *=10
        return step
