class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        A = str(A)
        end = len(A) - 1
        begin = 0
        while end >= begin:
            if A[begin] != A[end]:
                return False
            end -= 1
            begin += 1
        return True
