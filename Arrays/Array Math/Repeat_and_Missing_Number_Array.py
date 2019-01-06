#Without applying additional memory
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        
        n = len(A)
        
        sum_real =sum(A) 
        sum_square_real= 0
        
        for x in A:
            sum_square_real +=  x*x
            
        A_B = sum_real - (n*(n+1))//2
        
        
        A2_B2 = sum_square_real - (n*(n+1)*(2*n+1))//6
        
        A_plus_B = A2_B2/A_B
        
        missing = (abs(A_plus_B+A_B))/2
        
        repeat = (abs(A_plus_B - A_B))/2
        
        return [int(missing),int(repeat)]

'''
#Easy way to solve this problem but apply n memory complexity
from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        a_len = len(A)
        A = Counter(A)
        output = [0] * 2
        for i in range(1, a_len+1):
            A[i] -= 1
            if A[i] == 0:
                A.pop(i)
            elif A[i] == 1:
                output[0] = i
            else:
                output[1] = i
        return output
'''
