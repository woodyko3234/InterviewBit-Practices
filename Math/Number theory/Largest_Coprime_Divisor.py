class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        while True:
            temp=Solution.gcd(A,B)
            if temp==1:break
            A = A // temp 
        return A
    def gcd(a,b):
        if a==0:
            return b
        else:
            return Solution.gcd(b%a,a)
