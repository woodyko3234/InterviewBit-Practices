class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        while True:
            A1 = A;
            B1 = B;
            while B1>0:
                A1,B1 = B1,A1%B1;
            if A1==1:
                return A;
            A = A//A1;
