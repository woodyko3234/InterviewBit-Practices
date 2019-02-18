class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        A = str(A)
        for i in range(len(A)//2):
            if A[i] == A[-1-i]: continue
            else: return 0
        return 1
