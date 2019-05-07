class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if len(A) == 0 or len(A[0]) == 0:
            return ""
        minlen = len(A[0])
        for s in A:
            minlen = min(minlen, len(s))
        for i in range(minlen):
            w = A[0][i]
            for s in A:
                if s[i] != w:
                    return A[0][:i]
        return A[0][:i+1]
