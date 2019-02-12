class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        n = len(A)
        c=0
        m = max(A)
        for i in range(32):
            mask = 1<<i
            t = 0
            for a in A:
                if(mask&a):
                    t += 1
            c += (t*(n-t))
            #Set an if statement to break the loop so we don't need to look up to (2**32)-1 in every case.
            if m <= mask: break
        return (2*c)%1000000007
