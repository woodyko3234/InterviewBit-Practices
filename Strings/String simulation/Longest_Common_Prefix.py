class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        minlen = 10000000
        for i in range(len(A)):
            minlen = min(minlen, len(A[i]))
        count=0
        for i in range(minlen):
            c = A[0][i]
            for j in range(len(A)):
                if A[j][i] != c:
                    return A[0][:count]

            count+=1
        return A[0][:count]
