class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        n = len(A)
        if n <= 1: return A
        
        sorted_A = []
        for i in range(3):
            for j in range(n):
                if A[j] == i:
                    sorted_A.append(i)
        return sorted_A
