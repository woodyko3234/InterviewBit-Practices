import math

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        n = len(A)
        c=0
        for i in range(32):
            mask = 1<<i
            t = 0
            for a in A:
                if(mask&a):
                    t += 1
            c += (t*(n-t))
        return (2*c)%1000000007
