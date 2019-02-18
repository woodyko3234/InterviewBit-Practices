class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        A = str(A)
        if A[0] == "-":
            A = A[0] + A[:0:-1]
        else: A = A[::-1]
        #check overflow
        A = int(A)
        if A > 2**31-1 or A < -1*(2**31 - 1):
            return 0
        else:
            return A
