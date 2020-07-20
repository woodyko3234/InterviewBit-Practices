MOD = 10**9+7
class Solution:
    # @param A : integer
    # @return an integer
    
    def comb(self,l,n) :
        if 2*l > n : 
            return self.comb(n-l,n)
        c = 1
        for i in range(l):
            c = c*(n-i)//(i+1)
        return c
    
    def solve(self, A):
        ans,h = [1,1], 0
        for n in range(2,A+1):
            #define heap's height
            #2<<h: calculate the maximum
            if 2<<h <= n :
                h += 1
            #check how many nodes at the leaf layer
            m = n-(1<<h)+1
            #the actual nodes at the left subtree would be
            #the nodes between layer 1 to layer h-1 plus
            #the nodes at the left leaf layer
            l = (1<<(h-1))-1 + min(m,1<<(h-1))
            r = n - l - 1
            #calculate the combinations with recursion
            #ans[l] => recursion on the left subtree
            #ans[r] => recursion on the right subtree
            ans.append((self.comb(l,n-1)%MOD)*ans[l]%MOD*ans[r]%MOD)
        return ans[A]
