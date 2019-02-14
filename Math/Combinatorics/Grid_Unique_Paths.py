class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        A -=1;
        B-=1;
        num = A+B
        den = A
        res = 1
        for i in range(A):
            res *= (num-i)/(den-i)
        return int(round(res))
