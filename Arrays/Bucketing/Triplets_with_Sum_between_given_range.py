class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        n = len(A)
        
        a = float(A[0])
        b = float(A[1])
        c = float(A[2])
            
        for i in range (3,n):
            if ((a+b+c > 1) and (a+b+c < 2)):
                return 1
            elif a+b+c > 2:
                if (a>b and a>c):
                    a = float(A[i])
                elif (b>c and b>a):
                    b = float(A[i])
                elif (c>b and c>a):
                    c = float(A[i])
            else :
                if (a<b and a<c):
                    a = float(A[i])
                elif (b<c and b<a):
                    b = float(A[i])
                elif (c<b and c<a):
                    c = float(A[i])
        if ((a+b+c > 1) and (a+b+c < 2)):
            return 1
        return 0
