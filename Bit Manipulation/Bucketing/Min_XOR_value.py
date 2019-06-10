#Since s[i] ^ s[i - 2] > s[i] ^ s[i-1] / s[i+1] ^ s[i-1]
#It is possible to implement pair check
class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        s = sorted(A)
        minn = s[0]^s[1]
        for i in range(1,len(A)):
            if(s[i]^s[i-1]<minn):
                minn = s[i]^s[i-1]
        return minn
