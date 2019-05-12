class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        a_len = len(A)
        if a_len <= 1: return A
    
        begin = 0
        end = a_len
        max_len = 0
        max_substr = ""
        while begin < end and max_len < len(A[begin:end]):
            for i in range(begin, end):
                if A[i] == A[begin] and max_len < len(A[begin:i+1]):
                    mid = (begin + i+1) / 2.
                    if A[begin: int(mid)] == A[i: int(mid-0.5): -1]:
                        max_len = len(A[begin:i+1])
                        max_substr = A[begin:i+1]
            begin += 1
    
        return max_substr
